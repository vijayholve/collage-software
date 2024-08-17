from django.shortcuts import render,redirect ,get_object_or_404
from students.models import Timetable ,ClassGroup,Classes 
from .form import timetableform 


from django import template

register = template.Library()
@register.filter
def get_slot(timetable_entries, start_time, end_time, day):
    for entry in timetable_entries:
        if (entry.start_time == start_time and 
            entry.end_time == end_time and 
            entry.day_of_week == day):
            return entry
    return None

TemplateSyntaxError at /timetables/class-timetable/2/
get_item requires 2 arguments, 1 provided
Request Method:	GET
Request URL:	http://127.0.0.1:8000/timetables/class-timetable/2/
Django Version:	5.0.6
Exception Type:	TemplateSyntaxError
Exception Value:	
get_item requires 2 arguments, 1 provided
Exception Location:	C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\base.py, line 756, in args_check
Raised during:	timetables.views.class_timetable
Python Executable:	C:\Users\Vijay\python pro\attendance2\env\Scripts\python.exe
Python Version:	3.12.3
Python Path:	
['C:\\Users\\Vijay\\python pro\\attendance2',
 'C:\\Users\\Vijay\\python pro\\attendance2',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312\\Lib',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312',
 'C:\\Users\\Vijay\\python pro\\attendance2\\env',
 'C:\\Users\\Vijay\\python pro\\attendance2\\env\\Lib\\site-packages']
Server time:	Sat, 17 Aug 2024 07:48:02 +0000
Error during template rendering
In template C:\Users\Vijay\python pro\attendance2\templates\timetables\class_timetable.html, error at line 19

get_item requires 2 arguments, 1 provided
9	        <th>Wednesday</th>
10	        <th>Thursday</th>
11	        <th>Friday</th>
12	        <th>Saturday</th>
13	    </tr>
14	    {% for time_slot in time_slots %}
15	    <tr>
16	        <td>{{ time_slot.start_time }} - {{ time_slot.end_time }}</td>
17	        {% for day in days %}
18	            <td>
19	                {% with slot=timetable_dict|get_item:(time_slot.start_time, time_slot.end_time)|default:'' %}
20	                    {% if slot %}
21	                        {{ slot.subject.name }}<br>
22	                        {{ slot.teacher.name }}<br>
23	                        {{ slot.start_time }} - {{ slot.end_time }}
24	                    {% endif %}
25	                {% endwith %}
26	            </td>
27	        {% endfor %}
28	    </tr>
29	    {% endfor %}
Traceback Switch to copy-and-paste view
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\core\handlers\exception.py, line 55, in inner
                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\core\handlers\base.py, line 197, in _get_response
                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\timetables\views.py, line 76, in class_timetable
    return render(request, 'timetables/class_timetable.html', context)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\shortcuts.py, line 25, in render
    content = loader.render_to_string(template_name, context, request, using=using)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\loader.py, line 61, in render_to_string
        template = get_template(template_name, using=using)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\loader.py, line 15, in get_template
            return engine.get_template(template_name)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\backends\django.py, line 33, in get_template
            return Template(self.engine.get_template(template_name), self)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\engine.py, line 177, in get_template
        template, origin = self.find_template(template_name)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\engine.py, line 159, in find_template
                template = loader.get_template(name, skip=skip)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\loaders\cached.py, line 57, in get_template
            template = super().get_template(template_name, skip)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\loaders\base.py, line 28, in get_template
                return Template(
                            …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\base.py, line 154, in __init__
        self.nodelist = self.compile_nodelist()
                             ^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\base.py, line 196, in compile_nodelist
            return parser.parse()
                        ^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\base.py, line 510, in parse
                    raise self.error(token, e)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\base.py, line 508, in parse
                    compiled_result = compile_func(self, token)
                                           ^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\loader_tags.py, line 295, in do_extends
    nodelist = parser.parse()
                    ^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\python pro\attendance2\env\Lib\site-packages\django\template\base.py, line 510, in parse
                    raise self.error(token, e)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
def create_timetable_of_class(request,class_id):
    form=timetableform()
    if request.method == "POST":
        form=timetableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-classes')
    content={"form":form}
    return render(request,"timetables/create_timetables.html",content)
def timetable_of_class(request,classid):
    pass

def all_classes(request):
    classes = Classes.objects.all()
    class_ba=Classes.objects.get(name="BA")    
    years = ClassGroup.objects.filter(name=class_ba)
    class_id = request.GET.get('class')
    year_id = request.GET.get('year')

    if request.method ==  "GET" and class_id and year_id:
        class_obj=Classes.objects.get(id=class_id)
        classgroup=ClassGroup.objects.get(name=class_obj,year=year_id)
        return redirect("class-timetable", classgroup_id=classgroup.id) 
    # else:
    #     error(request,"Select the Value")
    content = {"classes": classes, "years": years}
    return render(request, "assignements/assignements_classes_list.html", content) 
def class_timetable(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, id=classgroup_id)
    timetable_entries = Timetable.objects.filter(classgroup=classgroup).order_by('day_of_week', 'start_time')

    # Prepare unique time slots
    time_slots = timetable_entries.values('start_time', 'end_time').distinct()

    # Structure data for the template
    timetable_dict = {}
    for entry in timetable_entries:
        key = (entry.start_time, entry.end_time)
        if key not in timetable_dict:
            timetable_dict[key] = {}
        timetable_dict[key][entry.day_of_week] = entry

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    context = {
        'classgroup': classgroup,
        'timetable_dict': timetable_dict,
        'time_slots': time_slots,
        'days': days
    }
    return render(request, 'timetables/class_timetable.html', context)
