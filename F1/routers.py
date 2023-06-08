class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'stats':
            return 'mySQL'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'stats':
            return 'mySQL'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'stats' or obj2._meta.app_label == 'stats':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'stats':
            return db == 'mySQL'
        return None