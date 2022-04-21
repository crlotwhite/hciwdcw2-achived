from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models.event import Event
from .models.store import Store
from .models.news import Deal, Announce
from .models.article import Article


# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ['logo_image']
    list_display = [
        'name',
        'store_type',
    ]

    def logo_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.logo.url,
            width=obj.logo.width,
            height=obj.logo.height,
        ))


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    readonly_fields = [
        'featured_image',
        'poster_image'
    ]
    list_display = [
        'title',
        'related_store_id',
    ]

    def featured_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.featured_image.url,
            width=obj.featured_image.width,
            height=obj.featured_image.height,
        ))

    def poster_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.poster.url,
            width=obj.poster.width,
            height=obj.poster.height,
        ))


@admin.register(Announce)
class AnnounceAdmin(admin.ModelAdmin):
    readonly_fields = [
        'featured_image',
        'poster_image'
    ]
    list_display = [
        'title',
    ]

    def featured_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.featured_image.url,
            width=obj.featured_image.width,
            height=obj.featured_image.height,
        ))

    def poster_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.poster.url,
            width=obj.poster.width,
            height=obj.poster.height,
        ))


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    change_list_template = 'admin/calender.html'

    def changelist_view(self, request, extra_context=None):
        import datetime
        import calendar

        from .event_calendar import EventCalendar

        after_day = request.GET.get('day__gte', None)
        extra_context = extra_context or {}

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
        previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
        previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                       day=1)  # find first day of previous month

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
        next_month = next_month + datetime.timedelta(days=1)  # forward a single day
        next_month = datetime.date(year=next_month.year, month=next_month.month, day=1)  # find first day of next month

        extra_context['previous_month'] = reverse('admin:shop_event_changelist') + '?event_start__gte=' + str(previous_month)
        extra_context['next_month'] = reverse('admin:shop_event_changelist') + '?event_start__gte=' + str(next_month)

        cal = EventCalendar()
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
        extra_context['calendar'] = mark_safe(html_calendar)
        return super(EventAdmin, self).changelist_view(request, extra_context)
