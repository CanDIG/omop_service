import django_filters
from .models import Person, ConditionOccurrence


class PersonFilter(django_filters.rest_framework.FilterSet):
    gender = django_filters.CharFilter(lookup_expr="iexact", field_name="gender_concept__concept_name",
                                       label="Gender")

    class Meta:
        model = Person
        fields = ["person_id", "gender", "year_of_birth", ]


class ConditionOccurrenceFilter(django_filters.rest_framework.FilterSet):
    condition = django_filters.CharFilter(lookup_expr="icontains",
                                          field_name="condition_concept__concept_name",
                                          label="Condition")
    condition_type = django_filters.CharFilter(lookup_expr="icontains",
                                               field_name="condition_type_concept__concept_name",
                                               label="Condition type")

    class Meta:
        model = ConditionOccurrence
        fields = ["condition_occurrence_id", "condition", "condition_type", ]
