insert into pet values ('01012341234','410846459730954', 141103, 'W', 'Cookie', 'Maltese', '5.3');
insert into pet values ('01037144918','410146805739832', 150506, 'M', 'Bebe', 'Pomeranian', '3.4');
insert into pet values ('01033453237','410397006766532', 130318, 'M', 'Coco', 'Toy Poodle', '3.2');
insert into pet values ('01004004392','410146532632766', 171226, 'W', 'Elsa', 'Bichon Frise', '4.5');
insert into pet values ('01040935392','410176654680532', 160829, 'M', 'Favian', 'Shih Tzu', '4.0');
insert into pet values ('01040935392','410805766146532', 140114, 'W', 'Gem', 'Maltese', '2.7');

insert into instructor values ('01032942346', 1990, 'Joy', 'W', 5);
insert into instructor values ('01010542346', 1992, 'Thomas', 'M', 3);
insert into instructor values ('01032944489', 1992, 'Linda', 'W', 3);

insert into disease values ('410146532632766','eczema');
insert into disease values ('410176654680532','eczema');
insert into disease values ('410176654680532','baldness');
insert into disease values ('410805766146532','dermatitis');
insert into disease values ('410805766146532','otitis externa');

insert into reservation values ('01012341234','01032942346','410846459730954',20201114,14);
insert into reservation values ('01037144918','01032942346','410146805739832',20201111,9);
insert into reservation values ('01033453237','01010542346','410397006766532',20201212,11);
insert into reservation values ('01004004392','01032944489','410146532632766',20201116,13);

insert into daily_log values ('410146805739832', '01037144918', 20200914, 'Y', 'Sweet pumpkin, tofu');
insert into daily_log values ('410397006766532', '01033453237', 20201010, 'Y', 'egg, carrot, fork');
insert into daily_log values ('410397006766532', '01033453237', 20201024, 'N', 'carrot, tofu');
insert into daily_log values ('410397006766532', '01033453237', 20201102, 'Y', 'chicken,egg');
insert into daily_log values ('410805766146532','01040935392',20201010,'Y','egg, carrot, fork');
insert into daily_log values ('410805766146532','01040935392',20201023,'N','fish, carrot');
insert into daily_log values ('410146532632766','01004004392',20201028,'Y','chicken,egg');
