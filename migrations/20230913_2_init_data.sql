-- Add basic task statuses.
begin;

insert into task_status (i_order, vc_name, next_status_id)
values (2, 'FINISHED', null)
returning id into next_id;

insert into task_status (i_order, vc_name, next_status_id)
values (1, 'IN_PROGRESS', next_id)
returning id into next_id;

insert into task_status (i_order, vc_name, next_status_id)
values (0, 'INITIAL', next_id);

commit;

-- Add admin user.
insert into user (vc_name) values ('admin');
