--FORD 사원과 같은 급여를 받는 사원의 사원번호를 검색하라.
SELECT EMPNO FROM EMP WHERE SAL = (SELECT SAL FROM EMP WHERE ENAME = 'FORD')AND NOT ENAME = 'FORD';

--부서별 인원수를 부서이름과 함께 사원이 많은 부서 순으로 검색하라.
select COUNT(*), dname from emp join dept on emp.deptno=dept.deptno GROUP by dname order by COUNT(*) desc;

--사원번호, 사원이름을 직속 부하직원수가 많은 순으로 검색하라.
select a.empno, a.ename from emp a, emp b where a.empno = b.mgr group by a.empno,a.ename order by count(*) desc;

--부서이름이 ‘SALES’이면서 사원직무가 ‘MANAGER’인 사원의 사원번호, 사원이름을 사원이름 순으로 검색하라.
select empno, ename from emp join dept using(deptno) where dname = 'SALES' AND JOB='MANAGER' ORDER BY ENAME;

--FORD 사원보다 많은 급여를 받는 사원 정보를 검색하라.
SELECT * FROM EMP WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'FORD');

--ALLEN 사원보다 적은 급여를 받는 사원 정보를 검색하라.
SELECT * FROM EMP WHERE SAL < (SELECT SAL FROM EMP WHERE ENAME = 'ALLEN');

--20번 부서 사원의 사원직무와 같은 사원직무인 다른 부서의 사원 정보를 검색하라.
SELECT * FROM EMP WHERE JOB IN (SELECT JOB FROM EMP WHERE DEPTNO = 20);

--전체 사원의 평균 급여보다 급여가 많은 사원 정보를 검색하라.
SELECT * FROM EMP WHERE SAL > (SELECT AVG(SAL) FROM EMP);

--급여가 모든 부서들의 평균 급여보다 많은 사원 정보를 검색하라.
SELECT * FROM EMP WHERE SAL > ALL(SELECT AVG(SAL) FROM EMP GROUP BY DEPTNO);

--20번 부서의 최대 급여보다 최대 급여가 큰 부서의 번호와 최대 급여를 검색하라.
SELECT DEPTNO, SAL FROM EMP WHERE SAL=(SELECT MAX(SAL) FROM EMP WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO = '20'));

--CHICAGO 지역에 위치하는 부서에 근무하는 사원 정보를 검색하라. 단, 부 질의를 이용한다.
SELECT * FROM EMP WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE LOC = 'CHICAGO');







