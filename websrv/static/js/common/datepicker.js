$(function() {

var holidays = {
    "0101":{type:0, title:"신정", year:""},
    "0301":{type:0, title:"삼일절", year:""},
    "0505":{type:0, title:"어린이날", year:""},
    "0606":{type:0, title:"현충일", year:""},
    "0815":{type:0, title:"광복절", year:""},
    "1003":{type:0, title:"개천절", year:""},
    "1009":{type:0, title:"한글날", year:""},
    "1225":{type:0, title:"크리스마스", year:""},
 
    "0209":{type:0, title:"설날", year:""},
    "0210":{type:0, title:"설날", year:""},
    "0211":{type:0, title:"설날", year:""},
    "0918":{type:0, title:"추석", year:""},
    "0919":{type:0, title:"추석", year:""},
    "0920":{type:0, title:"추석", year:""},
    "0517":{type:0, title:"석가탄신일", year:""}
};
 
jQuery(function($){
    $.datepicker.regional['ko'] = {
        closeText: '닫기',
        prevText: '이전달',
        nextText: '다음달',
        currentText: '오늘',
        monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
        monthNamesShort: ['1월','2월','3월','4월','5월','6월',
        '7월','8월','9월','10월','11월','12월'],
        dayNames: ['일','월','화','수','목','금','토'],
        dayNamesShort: ['일','월','화','수','목','금','토'],
        dayNamesMin: ['일','월','화','수','목','금','토'],
        weekHeader: 'Wk',
        dateFormat: 'yy-mm-dd',
        firstDay: 0,
        isRTL: false,
        showMonthAfterYear: true,
        yearSuffix: ''
    };
    $.datepicker.setDefaults($.datepicker.regional['ko']);
 
    $('.datepicker').datepicker({
        showOn: 'both',
        buttonImage: '',
        buttonImageOnly: false,
        buttonText: "달력",
        changeMonth: false,
        changeYear: false,
        showButtonPanel: false,
        yearRange: 'c-99:c+99',
		minDate: "0d",
        maxDate: '',
        beforeShowDay: function(day) {
            var result;
            // 포맷에 대해선 다음 참조(http://docs.jquery.com/UI/Datepicker/formatDate)
            var holiday = holidays[$.datepicker.formatDate("mmdd",day )];
            var thisYear = $.datepicker.formatDate("yy", day);
 
            // exist holiday?
            if (holiday) {
                if(thisYear == holiday.year || holiday.year == "") {
                    result =  [false, "date-holiday", holiday.title];
                }
            }
 
            if(!result) {
                switch (day.getDay()) {
                    case 0: // is sunday?
                        result = [false, "date-sunday"];
                        break;
                    case 6: // is saturday?
                        result = [true, "date-saturday"];
                        break;
                    default:
                        result = [true, ""];
                        break;
                }
            }
 
            return result;
        }
    });
});
  
});