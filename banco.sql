CREATE TABLE public.atividade
(
    id bigint,
    nome text,
    matricula text,
    PRIMARY KEY (id)
);

ALTER TABLE public.atividade
    OWNER to postgres;