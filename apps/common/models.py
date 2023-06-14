from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.query import F, Q
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.nowm)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RandomModel(BaseModel):
    """
    This is an example model, to be used as reference in the Styleguide,
    when discussing model validation via constraints.
    """
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="start_date_before_end_date",
                check=Q(start_date__lt=F("end_date"))
            )
        ]


class AbstractComment(BaseModel):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40

    COMMENT_STATUS_CHOICES = (
        (CREATED, 'Created'), (APPROVED, 'Approved'), (REJECTED, 'Rejected'), (DELETED, 'Deleted')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s')
    text = models.TextField()
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)s')
    # 'validated_by' shows who accepted the comment to be published
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=COMMENT_STATUS_CHOICES, default=CREATED)

    class Meta:
        abstract = True


class AbstractHotelOrHotelRoomFeature(BaseModel):
    title = models.CharField(max_length=80)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class AbstractHotelOrResidential(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city_or_section = models.CharField(max_length=100, verbose_name='City or Section')
    address = models.TextField()
    map_link = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(unique=True, validators=[
        RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.', 'invalid')])

    number_of_rooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                          verbose_name='Number of Rooms')
    floors = models.PositiveSmallIntegerField()
    capacity = models.IntegerField()
    area = models.IntegerField()
    # TODO
    #     gallery = models.OneToOneField(ResidentialGallery, on_delete=models.DO_NOTHING)

    is_valid = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AbstractReservation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_reservations')
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    modified_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True
