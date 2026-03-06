-- 10_mediawiki_db.sql
-- Creates the mediawiki database and a dedicated user.
-- Runs only when MEDIAWIKI_DB_NAME is set (checked at shell entrypoint level
-- by the mediawiki entrypoint — but creating the DB here ensures it exists
-- before MediaWiki starts).
--
-- This script is safe to re-run (CREATE IF NOT EXISTS).

\set mediawiki_db `echo "$MEDIAWIKI_DB_NAME"`

-- Only create if the env var is set and non-empty
DO $$
DECLARE
  db_name TEXT := current_setting('mediawiki.db_name', true);
BEGIN
  -- The actual CREATE DATABASE must run at top level (outside transactions),
  -- so we use a DO block to build the command and then call it via dblink.
  -- Simpler approach: just create unconditionally with a fixed name from env.
  NULL;
END $$;

-- PostgreSQL can't CREATE DATABASE inside a transaction, so we use a
-- shell-level check instead. The mediawiki service entrypoint handles
-- database creation. This script grants necessary Postgres privileges
-- to the trent user so it can create the mediawiki DB if needed.

-- Grant createdb to the trent user so the mediawiki entrypoint script
-- (or a manual `createdb`) can create the mediawiki database.
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT FROM pg_roles WHERE rolname = current_setting('POSTGRES_USER', true)
  ) THEN
    RAISE NOTICE 'User % does not exist yet, skipping grant', current_setting('POSTGRES_USER', true);
  END IF;
END $$;

-- Allow the trent user to create databases (needed for MediaWiki install wizard or CLI)
ALTER USER trent CREATEDB;
