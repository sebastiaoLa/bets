# Links:
# https://docs.djangoproject.com/en/1.11/ref/models/fields/#model-field-types
# https://tutorial.djangogirls.org/pt/

# 1. Criar ambiente virtual (linux)
virtualenv django

# 2. Acessar o ambiente virtual
source django/bin/activate

# 3. Instalar o Django
pip install django

# 4. Criar um projeto Django
django-admin startproject {NOME_PROJETO}
cd {NOME_PROJETO}

# 5. Aplicar o arquivo de migração
python manage.py migrate

# 6. Executar o projeto
python manage.py runserver

# 7. Criar usuário administrativo
python manage.py createsuperuser

# 8. Criar aplicação
python manage.py startapp {NOME_APP}

# 9. Adicionar a aplicação no arquivo de configurações
# 9.1 Abrir o arquivo settings.py, localizado na pasta {NOME_PROJETO}/
# 9.2 Adicionar o nome da aplicação na lista chamada INSTALLED_APPS

# 10. Models: criar primeiro modelo
class Player(models.Model):

    name = models.CharField(
        'nome',
        max_length=255
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'apostador'
        verbose_name_plural = 'apostadores'
        ordering = ['name']

# 10.1 Após criar o model, você deve criar o arquivo de migração do banco de dados
python manage.py makemigrations

# 10.2 Em seguida você deve aplicar o arquivo de migração
python manage.py migrate
