-- Table: public.user

DROP TABLE IF EXISTS public."users";
CREATE TABLE IF NOT EXISTS public."users"
(
    id integer NOT NULL,
    name character(1)[] COLLATE pg_catalog."default" NOT NULL,
    email character(1)[] COLLATE pg_catalog."default" NOT NULL,
    password character(1)[] COLLATE pg_catalog."default" NOT NULL,
    date_created date,
    last_updated date,
    CONSTRAINT user_pkey PRIMARY KEY (id)
)

-- TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."users"
    OWNER to postgres;

COMMENT ON TABLE public."users"
    IS 'This will contain user information for this blog project.';
	
DROP TABLE IF EXISTS public."posts";
CREATE TABLE IF NOT EXISTS public."posts"
(
	id integer NOT NULL,
    title character(1)[] COLLATE pg_catalog."default" NOT NULL
);
-- TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."posts"
    OWNER to postgres;

COMMENT ON TABLE public."posts"
    IS 'This will contain the blog posts.';
