from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):
    ocupacao = models.CharField(max_length = 100, verbose_name = "Ocupação")

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Pessoa")
    pai = models.CharField(max_length = 100, verbose_name = "Nome do Pai")
    mae = models.CharField(max_length = 100, verbose_name = "Nome da Mãe")
    cpf = models.CharField(max_length = 14, verbose_name = "CPF")
    email = models.EmailField(max_length = 100, verbose_name = "EMAIL", unique = True)
    data_nasc = models.DateField(verbose_name = "Data de Nascimento")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name = "Ocupação")

    def __str__(self):
        return self.nome
    
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da instituição")
    site = models.URLField(max_length = 254, verbose_name = "Link do Site")
    telefone = models.CharField(max_length = 20, verbose_name = "Telefone")
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, verbose_name = "Cidade da Instituição")

class AreaSaber(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Area Saber")

class Curso(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do Curso")
    carga_horaria_total = models.DurationField(verbose_name = "Carga Horária total")
    duracao_meses = models.PositiveIntegerField(verbose_name = "Duração do Curso")
    areasaber = models.ForeignKey(AreaSaber, on_delete = models.CASCADE, verbose_name = "Area do Saber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete = models.CASCADE, verbose_name = "Instituição de Ensino")

class Turma(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Turma")

class Disciplina(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Disciplina")
    areasaber = models.ForeignKey(AreaSaber, on_delete = models.CASCADE, verbose_name = "Area do Saber")

class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete = models.CASCADE, verbose_name = "Instituição")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Nome do Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Pessoa")
    data_inicio = models.DateField(verbose_name = "Data de Inicio")
    data_previsao_termino = models.DateField(verbose_name = "Data de Previsão de Termino")

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Tipo de Avaliação")

class Avaliacao(models.Model):
    descricao = models.CharField(max_length = 100, verbose_name = "Descrição")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Curso")
    avaliacaotipo = models.ForeignKey(AvaliacaoTipo, on_delete = models.CASCADE, verbose_name = "Tipo de Avaliação")

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Curso")
    pessoa = models.ForeignKey(Pessoa,
    on_delete = models.CASCADE, verbose_name = "Pessoa")
    numero_faltas = models.PositiveIntegerField(verbose_name = "Numero de Faltas")

class Turnos(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Turnos")

class Ocorrencias(models.Model):
    descricao = models.CharField(max_length = 300, verbose_name = "Descrição da Ocorrencia/Advertencia")
    data = models.DateField(verbose_name = "Data da Ocorrencia/Advertencia")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Curso")
    pessoa = models.ForeignKey(Pessoa,
    on_delete = models.CASCADE, verbose_name = "Pessoa")

class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Curso")
    carga_horaria = models.DurationField(verbose_name = "Carga Horária")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso")
    periodo = models.ForeignKey(Turma, on_delete = models.CASCADE, verbose_name = "Periodo")

# Create your models here.