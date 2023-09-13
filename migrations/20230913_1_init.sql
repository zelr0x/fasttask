-- Run this first:

-- create user fasttask with password 'fasttask';
-- create database fasttask;
-- grant usage on schema public to fasttask;
-- \c fasttask;
-- create extension if not exists "uuid-ossp";

-- TODO: add separate table for projects
-- TODO: add separate table for task types
-- TODO: add separate table for allowed task status transitions (with project and task type fks)
-- TODO: remove postgres non-local password login (probably via pg_hba.conf)

create table if not exists user (
    id uuid not null default uuid_generate_v4()
        constraint pk_user primary key default uuid_generate_v1mc(),
    dt_created_at timestamptz not null default now(),
    dt_updated_at timestamptz not null default now(),
    vc_name varchar(255) not null
);

create table if not exists task_status (
    id uuid not null default uuid_generate_v4()
        constraint pk_task_status primary key,
    dt_created_at timestamptz not null default now(),
    dt_updated_at timestamptz not null default now(),
    i_order int not null default 0
        constraint uk_task_status_i_order unique (i_order),
    vc_name varchar(64) not null,
    next_status_id not null
        constraint fk_task_status_next_status foreign key references task_status (id)
);

create table if not exists task (
    id uuid not null default uuid_generate_v4()
        constraint pk_task primary key,
    dt_created_at timestamptz not null default now(),
    dt_updated_at timestamptz not null default now(),
    author_id uuid not null 
        constraint fk_task_author foreign key references user (id),
    vc_title varchar(255) not null,
    task_status not null
        default (select id from task_status where b_initial = true),
    vc_description text,
    assignee_id uuid
        constraint fk_task_assignee foreign key references user (id)
);

grant select, insert, update, deleteon all tables in schema public to fasttask;
