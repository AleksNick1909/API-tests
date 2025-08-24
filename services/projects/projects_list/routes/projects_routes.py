from config.links import Links


class ProjectsRoutes:

    projects_list = f'{Links.API}/construction-objects'
    get_projects_list = f'{projects_list}/constructions-registry/tier'
    construction = '/constructions'
