"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from Student import views as stdview
from Transport import views as traview
from Hostel import views as hosview
from Library import views as libview
from Events import views as eveview
from Academics import views as acaview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',stdview.home,name='home'),
    url(r'^student$',stdview.studentapp,name='student'),
    url(r'^grade/$',stdview.student_grade,name='std_grade'),
    url(r'^addgrade/$',stdview.add_grade,name='add_grade'),
    url(r'^faculty/$',stdview.student_faculty,name='student_faculty'),
    url(r'^addfaculty/$',stdview.add_faculty,name='add_faculty'),
    url(r'^studentlist/$',stdview.student_list,name='std_list'),
    url(r'^addstudent/$',stdview.add_student,name='add_student'),
    url(r'^gradelistapi$', stdview.GradeList.as_view()),
    url(r'^facultylistapi$', stdview.FacultyList.as_view()),
    url(r'^studentlistapi$', stdview.StudentList.as_view()),

    url(r'^vehiclelist/$',traview.Vehicle_list,name='vehicle_list'),
    url(r'^addvehicle/$',traview.add_vehicle,name='add_vehicle'),
    url(r'^routelist/$',traview.Route_list,name='route_list'),
    url(r'^addroute/$',traview.add_route,name='add_route'),
    url(r'^driverlist/$',traview.Driver_list,name='driver_list'),
    url(r'^adddriver$',traview.add_driver,name='add_driver'),
    url(r'^talist/$',traview.Transport_Allocation_list,name='ta_list'),
    url(r'^addta$',traview.add_ta,name='add_ta'),
    url(r'^transport$',traview.transportapp,name='transport'),
    url(r'^vehicleapi$', traview.VehicleListAPI.as_view()),
    url(r'^routeapi$', traview.RouteListAPI.as_view()),

    url(r'^hosteldetails/$',hosview.Hostel_Detail,name='Hostel_Details'),
    url(r'^addhosteldetails/$',hosview.add_hostel_details,name='add_hostel_details'),
    url(r'^hostelroom/$',hosview.getHostelRoom,name='Hostel_Room'),
    url(r'^addhostelrooms/$',hosview.add_hostel_room,name='add_hostel_room'),
    url(r'^hostelregister/$',hosview.HostelRegister,name='Hostel_Register'),
    url(r'^addhostelregister/$',hosview.add_hostel_regester,name='add_hostel_regester'),
    url(r'^hostelallocation/$',hosview.HostelAllocation,name='Hostel_Allocation'),
    url(r'^addhostelallocation/$',hosview.add_hostelallocation,name='add_hostelallocation'),
    url(r'^hostel$',hosview.hostelapp,name='hostel'),
    url(r'^hosteldetailsapi$', hosview.HostelDetailList.as_view()),
    url(r'^hostelroomapi$', hosview.HostelRoomList.as_view()),
    url(r'^hostelregapi$', hosview.HostelRegList.as_view()),

    url(r'^bookcategory/$',libview.getCategory,name='Book_category'),
    url(r'^addcatagory/$',libview.add_catagory,name='add_catagory'),
    url(r'^book/$',libview.getBook,name='Book'),
    url(r'^addbook/$',libview.add_book,name='add_book'),
    url(r'^issuebook/$',libview.Issue_Book,name='Issue_Book'),
    url(r'^addissue/$',libview.add_issues,name='add_issues'),
    url(r'^returnbook/$',libview.Return_Book,name='Return_Book'),
    url(r'^addreturn/$',libview.add_return,name='add_return'),
    url(r'^library$',libview.libraryapp,name='Library'),
    url(r'^bookapi$', libview.BookList.as_view()),
    url(r'^categoryapi$', libview.CategoryList.as_view()),

    url(r'^eventtype/$',eveview.getEventType,name='Event_Type'),
    url(r'^addeventtype/$',eveview.add_eventtype,name='add_eventtype'),
    url(r'^eventlist/$',eveview.getEvent,name='Event'),
    url(r'^addevent/$',eveview.add_event,name='add_event'),
    url(r'^events$',eveview.eventsapp,name='events'),
    url(r'^eventlistapi$', eveview.EventList.as_view()),

    url(r'^addcourse/$',acaview.add_course,name='add_course'),
    url(r'^addbatch/$',acaview.add_batch,name='add_batch'),
    url(r'^addsubject/$',acaview.add_subject,name='add_subject'),
    url(r'^addexam/$',acaview.add_exam,name='add_exam'),
    url(r'^addassignment/$',acaview.add_assignment,name='add_assignment'),
    url(r'^addnotes/$',acaview.add_notes,name='add_notes'),
    url(r'^addcertificates/$',acaview.add_certificate,name='add_certificate'),
    url(r'^addalumni/$',acaview.add_alumni,name='add_alumni'),
    url(r'^course/$',acaview.getCourse,name='Course'),
    url(r'^batch/$',acaview.getBatch,name='Batch'),
    url(r'^subject/$',acaview.getSubject,name='subject'),
    url(r'^exam/$',acaview.getExam,name='exam'),
    url(r'^assignment/$',acaview.getAssignment,name='assignment'),
    url(r'^notes/$',acaview.getNotes,name='notes'),
    url(r'^certificates/$',acaview.getCertificate,name='certificate'),
    url(r'^alumni/$',acaview.getAlumni,name='alumni'),
    url(r'^academics$',acaview.academicsapp,name='academics'),
    url(r'^courseapi$', acaview.CourseListAPI.as_view()),
    url(r'^batchapi$', acaview.BatchListAPI.as_view()),
    url(r'^subjectapi$', acaview.SubjectListAPI.as_view()),


]
