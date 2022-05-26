from django.urls import path

from . import views

urlpatterns = [
    path(''                      , views.index               , name='index'              ),
    path('all_blogs/'            , views.index               , name='index'              ),
    path('blog/<str:blog>'       , views.index               , name='blog'               ),
    path('registration/'         , views.registration        , name='registration'       ),
    path('reg_submit/'           , views.submit_registration , name='registration_submit'),
    path('login/'                , views.login               , name='login'              ),
    path('login_/'               , views.no_login            , name='no_login'           ),
    path('log_submit/'           , views.submit_login        , name='login_submit'       ),
    path('logout/'               , views.logout              , name='logout'             ),
    path('change_password/'      , views.change_password     , name='change_password'    ),
    path('npw_submit/'           , views.submit_change       , name='change_submit'      ),
    path('create_blog/'          , views.new_blog            , name='new_blog'           ),
    path('article/<int:aid>'     , views.article             , name='article'            ),
    path('new_article/'          , views.new_article         , name='new_article'        ),
    path('edit_article/<int:aid>', views.edit_article        , name='edit_article'       ),
    path('article_submit/'       , views.submit_article      , name='article_submit'     ),
    path('media/<str:img>'       , views.get_img             , name='get_img'            ),
]