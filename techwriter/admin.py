from django.contrib import admin
from django.core.mail import send_mail
from .models import Client, Status, Article


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry_type', 'email')

    actions = ['send_notification_email']

    def send_notification_email(self, request, queryset):
        for client in queryset:
            # Assuming clients have an email field
            send_mail(
                'Notification',  # Subject
                'Your new article is ',  # Message
                'from@example.com',  # Sender email
                [client.email],  # Recipient email
                fail_silently=True,
            )
        self.message_user(request, f"Notification email sent to {queryset.count()} clients.")
    send_notification_email.short_description = "Send notification email to selected clients"


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'client', 'status', 'deadline', 'last_modification_date')
    list_filter = ('status', 'author', 'client')
    search_fields = ('title', 'content')

    # Custom admin action to submit an article
    actions = ['submit_articles']

    def submit_articles(self, request, queryset):
        # Assuming 'Submitted' is a status value in the Status model
        submitted_status = Status.objects.get(name='Published')
        queryset.update(status=submitted_status)
        self.message_user(request, f"{queryset.count()} articles Published successfully.")
    submit_articles.short_description = "Published selected articles"


# Registering the models with the admin
admin.site.register(Client, ClientAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Article, ArticleAdmin)
