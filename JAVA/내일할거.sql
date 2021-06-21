#삽입 쿼리
INSERT INTO `product` (`code`, `pname`, `cost`, `pnum`, `jnum`, `sale`, `gcode`) 
VALUES ('C03', '냉장고냉동박스', '3500', '300', '80', '4000', 'C');

#제품 코드를 통해 조회해야함
select * from product, groupcode where product.gcode=groupcode.gcode and code = 'A01';



#우선생산 제품 조회 제품이름, 생산수량 (재고수량이 목표수량의 20%미만)
select pname, pnum-jnum as 생산수량  from product where jnum<(pnum*0.2);



#현 재고의 제품을 모두 판매하였을때 수익순으로 
select pname, jnum*(sale-cost) as 수익  from product order by 수익 desc;



#그룹별 재고수량 출력
select gcode, sum(jnum) from product GROUP by gcode;

#제품코드로 조회후 수정해야한다.
update product set pname='컴퓨터모니터1',cost=50001, pnum=401, jnum=51, sale=55001, gcode='B'
where code = 'A03';


#항목삭제
delete from product where code='A03';





