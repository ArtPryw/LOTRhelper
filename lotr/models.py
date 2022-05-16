from django.db import models


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    #posiadane postaci

class Fraction(models.Model):

    name = models.CharField(max_length=50)
    hp = models.FloatField(default=0)
    describe = models.CharField(max_length=250)
    focus = models.IntegerField(default=1)  # coś jak mana/dla łuczników też potrzebne
    condition = models.IntegerField(default=1)  # do zadawania ataków ze skilli
    min_dmg_physical = models.FloatField(default=1.0)
    max_dmg_physical = models.FloatField(default=2.0)
    min_dmg_magical = models.FloatField(default=0.5)
    max_dmg_magical = models.FloatField(default=0.75)
    self_heal = models.IntegerField(default=5)  # leczenie na każdy dzień - zakres 0-10. Przy 5 choroby nie postępują, ale też nie są leczone samodzielnie, można zrobić skilla który będzie uruchamiał samolecezenie w walce
    armor = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)  # max 10
    thievery = models.IntegerField(default=0)  # ile można ukraść, max 10, min -10
    stealh = models.IntegerField(default=0)  # chodzienie niezauważonym, max10, min -10
    accuracy = models.IntegerField(default=0)  # modyfikator ataku fizycznego dla klas związanych z łukami
    strength = models.IntegerField(default=0)  # modyfikator ataku fizycznego dla walczących wręcz
    wit = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ClassChar(models.Model):
    name = models.CharField(max_length=50)
    hp = models.FloatField(default=0)
    describe = models.CharField(max_length=250)
    focus = models.IntegerField(default=1)  # coś jak mana/dla łuczników też potrzebne
    condition = models.IntegerField(default=1)  # do zadawania ataków ze skilli
    min_dmg_physical = models.FloatField(default=1.0)
    max_dmg_physical = models.FloatField(default=2.0)
    min_dmg_magical = models.FloatField(default=0.5)
    max_dmg_magical = models.FloatField(default=0.75)
    self_heal = models.IntegerField(default=5)  # leczenie na każdy dzień - zakres 0-10. Przy 5 choroby nie postępują, ale też nie są leczone samodzielnie, można zrobić skilla który będzie uruchamiał samolecezenie w walce
    armor = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)  # max 10
    thievery = models.IntegerField(default=0)  # ile można ukraść, max 10, min -10
    stealh = models.IntegerField(default=0)  # chodzienie niezauważonym, max10, min -10
    accuracy = models.IntegerField(default=0)  # modyfikator ataku fizycznego dla klas związanych z łukami
    strength = models.IntegerField(default=0)  # modyfikator ataku fizycznego dla walczących wręcz
    wit = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Character(models.Model):
    char_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    fraction_key = models.ForeignKey(Fraction, on_delete=models.DO_NOTHING)
    class_key = models.ForeignKey(ClassChar, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=40)
    #do wyjebki class name
    class_name = models.CharField(max_length=50)
    fraction_name = models.CharField(max_length=50)

    hp = models.FloatField(default=0)
    story = models.CharField(max_length=350)
    focus = models.IntegerField(default=0)  # coś jak mana/dla łuczników też potrzebne
    condition = models.IntegerField(default=0)  # do zadawania ataków ze skilli
    min_dmg_physical = models.FloatField(default=0.0)
    max_dmg_physical = models.FloatField(default=0.0)
    min_dmg_magical = models.FloatField(default=0.0)
    max_dmg_magical = models.FloatField(default=0.0)
    self_heal = models.IntegerField(default=0)  # leczenie na każdy dzień - zakres 0-10. Przy 5 choroby nie postępują, ale też nie są leczone samodzielnie, można zrobić skilla który będzie uruchamiał samolecezenie w walce
    armor = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)  # max 10
    thievery = models.IntegerField(default=0)  # ile można ukraść, max 10, min -10
    stealh = models.IntegerField(default=0)  # chodzienie niezauważonym, max10, min -10
    accuracy = models.IntegerField(default=0)  # modyfikator ataku fizycznego dla klas związanych z łukami
    strength = models.IntegerField(default=0)  # modyfikator ataku fizycznego dla walczących wręcz
    wit = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:  # object is being created, thus no primary key field yet
            self.hp = self.hp + self.fraction_key.hp + self.class_key.hp
            self.focus += self.fraction_key.focus + self.class_key.focus
            self.condition += self.fraction_key.condition + self.class_key.condition
            self.min_dmg_physical += self.fraction_key.min_dmg_physical + self.class_key.min_dmg_physical
            self.max_dmg_physical += self.fraction_key.max_dmg_physical + self.class_key.max_dmg_physical
            self.min_dmg_magical += self.fraction_key.min_dmg_magical + self.class_key.min_dmg_magical
            self.max_dmg_magical += self.fraction_key.max_dmg_magical + self.class_key.max_dmg_magical
            self.self_heal +=self.fraction_key.self_heal + self.class_key.self_heal
            self.armor += self.fraction_key.armor + self.class_key.armor
            self.charisma += self.fraction_key.charisma + self.class_key.charisma
            self.thievery +=self.fraction_key.thievery + self.class_key.thievery
            self.stealh +=self.fraction_key.stealh + self.class_key.stealh
            self.accuracy += self.fraction_key.accuracy + self.class_key.accuracy
            self.strength += self.fraction_key.strength + self.class_key.strength
            self.wit +=  self.fraction_key.wit + self.class_key.wit
        super(Character, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
