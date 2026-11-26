# The actual symmetric closing height is below seven tenths

Private written geometric deduction, 9 November 2026. The original
positive symmetric \(343\) solution lies strictly inside the taller
inner-source rectangle. The proof retains both components of the
original cubic and the unsquared middle return. It selects no root
of a new elimination polynomial and makes no numerical evaluation.

## 1. Original point and statement

Use the actual positive solution and notation of the
[angle and height box](research_mixed_symmetric_closing_angle_and_height_box.md):
\[
 t_g=a-iH,\quad u_g=\beta-iK,\quad
 c=\cos(t_g/2)=p+iq,\quad C=\cos(u_g/2),\quad
 L=\cosh K,\quad S=\sinh K,\quad B=\cos\beta .
 \tag{1}
\]
That theorem, on the original logarithmic sheet, proves
\[
 0<B<1,\qquad 17/30<K<5/6,\qquad
 3/4<p<6/7,\quad1/4<q<7/20,
 \qquad |c|<1,\quad |C|<1,\quad S<1 .
 \tag{2}
\]
The two exact middle identities and the end cubic are
\[
 p=S\left(B+\frac1{L-B}\right),\qquad
 q=\sqrt{1-B^2}\left(L-\frac1{L-B}\right),
 \tag{3}
\]
\[
 \begin{split}
 C_R&=p(4p^2-12q^2+8q-3),\\
 C_I&=F_p(q):=(12q-4)p^2-4q^3+4q^2-3q+1,\\
 C_R^2&=(L+1)(1+B)/4,\qquad
 C_I^2=(L-1)(1-B)/4,\qquad C_R,C_I>0 .
 \end{split}
 \tag{4}
\]
These are consequences of the already specified original returns,
not a substitute squared stationary system.

**Theorem.** The actual symmetric closing point satisfies
\[
 \boxed{\qquad0<\beta<\pi/2,\qquad17/30<K<7/10.\qquad}
 \tag{5}
\]
In particular the outgoing angle belongs to the interior of the
taller lower rectangle. This is a geometric localization result.
It does not itself prove that the corresponding closing saddle
contributes to the full outer finite trace.

## 2. Monotonicities and elementary height witnesses

The following uses the positive branch in (2)--(4).
For fixed \(L\), the right side for \(p\) in (3) increases
strictly with \(B\). Where the right side for \(q\) is positive,
it decreases strictly with \(B\):
\[
 \partial_Bp=S\{1+(L-B)^{-2}\}>0,\qquad
 \partial_Bq=
 -\frac{B}{\sqrt{1-B^2}}\left(L-\frac1{L-B}\right)
 -\frac{\sqrt{1-B^2}}{(L-B)^2}<0.
 \tag{6}
\]
For fixed \(B\), the \(q\) expression increases with \(K\).
For \(p\),
\[
 \partial_Kp=LB+\frac{1-LB}{(L-B)^2}>0
                               \quad\hbox{if }LB<1.
 \tag{7}
\]
Every fixed comparison value of \(B\) below is at most \(1/4\).
Since \(L<\sqrt2\), condition (7) holds on every such comparison
segment. Thus the height comparisons never require an extension
of the original stationary solution.

We record the required elementary bounds:
\[
 \begin{array}{lll}
 \sinh(3/4)>105/128,&\quad \cosh(3/4)<13/10,\\
 \sinh(18/25)>39/50,&\quad \cosh(18/25)<51/40,\\
 \sinh(7/10)>91/120>151/200>3/4,
 &\quad 251/200<\cosh(7/10)<157/125<13/10 .
 \end{array}
 \tag{8}
\]
All are positive-series witnesses. For clarity, when \(x>0\)
and \(x^2<30\),
\[
 \cosh x\le1+x^2/2+\frac{x^4/24}{1-x^2/30}.
 \tag{9}
\]
At \(x=3/4\) this is
\[
 41/32+135/10048<13/10,
 \tag{10}
\]
since \(21600<30144\). At \(x=18/25\), it is
\[
 787/625+4374/383875<51/40,
 \tag{11}
\]
where \(21870000<30326125\) compares the last term with
\(79/5000\). At \(x=7/10\), it is
\[
 249/200+2401/236080<157/125,
 \tag{12}
\]
where \(2401000<2596880\) compares the last term with \(11/1000\).
The lower fourth-order bound is
\[
 \cosh(7/10)>1+49/200+2401/240000
                 =301201/240000>251/200.
 \tag{13}
\]
The first two hyperbolic-sine bounds use
\(\sinh x>x+x^3/6\):
\[
 3/4+(3/4)^3/6=105/128,\qquad
 18/25+(18/25)^3/6=12222/15625>39/50 .
 \tag{14}
\]
The final one keeps the fifth-order term:
\[
 \sinh(7/10)>
 7/10+(7/10)^3/6+(7/10)^5/120
        =9102807/12000000>91/120 .
 \tag{15}
\]
The last comparison is \(9102807>9100000\).

The imaginary cubic \(F_p\) is strictly increasing for
\(0\le q\le3/5\), as proved in the angle-box theorem:
\[
 F_p'(q)>15/4+8q-12q^2>0.
 \tag{16}
\]
All occurrences below lie in that interval.

## 3. First bootstrap: \(K<3/4\) and \(q<1/3\)

Suppose \(K\ge3/4\). If \(B\ge1/6\), (6)--(8) give
\[
 p\ge p(3/4,1/6)>
 \frac{105}{128}\left(\frac16+\frac{15}{17}\right)
       =\frac{11235}{13056}>\frac67 .
 \tag{17}
\]
The final comparison is \(78645>78336\), contradicting (2).
If \(B\le1/6\), the positive \(q\) expression instead gives
\[
 q\ge q(3/4,1/6)>
 \frac{19}{20}\left(\frac{41}{32}-\frac{96}{107}\right)
       =\frac{24985}{68480}>\frac7{20}.
 \tag{18}
\]
Here \(L>41/32\), \(\sqrt{35}/6>19/20\), and the function
\(L-(L-1/6)^{-1}\) is increasing. The strict positivity of
the displayed lower bound also licenses (6) throughout the
comparison interval. Its last comparison is
\(24985>23968\). This is the other contradiction to (2).
Thus \(K<3/4\).

Consequently
\[
 C_I=\sin(\beta/2)\sinh(K/2)
 <\frac1{\sqrt2}\sinh(3/8)
 <\frac34\frac{48}{125}
       =\frac{36}{125}<\frac8{27}.
 \tag{19}
\]
The bound \(\sinh(3/8)\le48/125\) follows from
\(\sinh x\le x/(1-x^2/6)\); the last comparison is \(972<1000\).
But \(F_p(1/3)=8/27\), independently of \(p\). Equation
(16) therefore gives \(q<1/3\).

## 4. Consequences of supposing \(K\ge7/10\)

Assume from now on that \(K\ge7/10\), seeking a contradiction.
By (8) and Section 3,
\[
       S>151/200,\qquad 251/200<L<13/10,\qquad
                         1/4<q<1/3 .
 \tag{20}
\]

First \(B<1/4\). Otherwise the first middle identity gives
\[
 p>\frac34\left(\frac14+\frac{20}{21}\right)
                   =\frac{101}{112}>\frac67 .
 \tag{21}
\]
Thus \(C_R^2<23/32\). On \(1/4<q<1/3\),
\(-12q^2+8q-3\ge-7/4\). If \(p\ge5/6\), the real
cubic would give
\[
 C_R\ge p(4p^2-7/4)\ge185/216>\sqrt{23/32},
 \tag{22}
\]
a contradiction. The polynomial in \(p\) is increasing for
\(p>3/4\); the last squared comparison is
\(1095200>1073088\). We have proved \(p<5/6\).

Next \(B<1/5\). Indeed if \(B\ge1/5\), (20) yields
\[
 p>\frac{151}{200}\left(\frac15+\frac{10}{11}\right)
                      =\frac{9211}{11000}>\frac56,
 \tag{23}
\]
where \(55266>55000\). In particular,
\[
 C_R^2<69/100,\qquad
 C_I^2>\frac{49}{1000}>\frac1{25}.
 \tag{24}
\]
The second inequality only uses \(L>249/200\) and \(1-B>4/5\).

These bounds force \(q>3/10\). If not, (16) and \(p>3/4\)
give
\[
 C_I\le F_p(3/10)
       <-\frac25\frac9{16}+\frac{44}{125}
        =\frac{127}{1000}<\frac15,
 \tag{25}
\]
contradicting (24). On the resulting interval
\(3/10<q<1/3\),
\[
                    -12q^2+8q-3\ge-42/25.
 \tag{26}
\]
If \(p\ge33/40\), the real cubic and its increasing \(p\)
polynomial would give
\[
 C_R\ge p(4p^2-42/25)
       \ge\frac{13761}{16000}>\sqrt{69/100}.
 \tag{27}
\]
The exact squared comparison is \(189365121>176640000\).
Therefore
\[
                 B<1/5,\quad 3/10<q<1/3,\quad p<33/40 .
 \tag{28}
\]

## 5. A second height bootstrap and the stricter imaginary bound

Still under the supposition \(K\ge7/10\), we first prove
\(K<18/25\). If \(K\ge18/25\) and \(B\ge1/6\), then
\[
 p\ge p(18/25,1/6)>
 \frac{39}{50}\left(\frac16+\frac{120}{133}\right)
       =\frac{33267}{39900}>\frac{33}{40}.
 \tag{29}
\]
The cleared comparison is \(1330680>1316700\).
If \(B\le1/6\), use \(L>787/625\) and
\(\sqrt{35}/6>59/60\) to obtain
\[
 q\ge q(18/25,1/6)>
 \frac{59}{60}\left(\frac{787}{625}-\frac{3750}{4097}\right)
       =\frac{59}{60}\frac{880589}{2560625}>\frac13 .
 \tag{30}
\]
The last comparison is \(155864253>153637500\).
Both alternatives contradict (28). Hence
\[
                     K<18/25,\qquad L<51/40.
 \tag{31}
\]

The bound \(q<1/3\) also forces \(B>3/20\). For if \(B\le3/20\),
use \(L>5/4\) in (3) and its monotonicities:
\[
 q>
 \frac{\sqrt{391}}{20}
       \left(\frac54-\frac{10}{11}\right)
       =\frac{15\sqrt{391}}{880}>\frac13 .
 \tag{32}
\]
The squared comparison is \(791775>774400\).
Together with (31) this proves
\[
                    C_I^2<\frac{187}{3200}.
 \tag{33}
\]

At \(q=13/40\), the coefficient \(12q-4\) is \(-1/10\).
Using \(p<33/40\) from (28), one has
\[
 F_p(13/40)>
 -\frac1{10}\frac{1089}{1600}
             +\frac{4963}{16000}
       =\frac{1937}{8000}>\sqrt{\frac{187}{3200}} .
 \tag{34}
\]
For the last strict inequality,
\(1937^2=3751969>3740000\).
Equations (16),(33),(34) therefore imply
\[
                             q<13/40 .
 \tag{35}
\]

## 6. The final incompatible real bounds

The stricter imaginary bound (35) forces \(B>1/6\).
Indeed if \(B\le1/6\), use \(L>251/200\) from (20):
\[
 \begin{split}
 q&>
 \frac{59}{60}\left(\frac{251}{200}-\frac{600}{653}\right)
   =\frac{2590277}{7836000}>\frac{13}{40}.
 \end{split}
 \tag{36}
\]
The last comparison is \(2590277>2546700\).

By (7),(8), \(B>1/6\) and \(K\ge7/10\) now give
\[
 p>p(7/10,1/6)>
 \frac{91}{120}\left(\frac16+\frac{750}{817}\right)
      =\frac{483847}{588240}>\frac{41}{50}.
 \tag{37}
\]
Here \(251/200<L(7/10)<157/125\), and the last comparison
is \(24192350>24117840\).

On the one hand, \(B<1/5\) and \(L<51/40\) give
\[
                          C_R^2<273/400.
 \tag{38}
\]
On the other, \(q>3/10\) and (26),(37) in the real cubic yield
\[
 C_R>p(4p^2-42/25)>
 \frac{41}{50}\left(\frac{1681}{625}-\frac{42}{25}\right)
       =\frac{25871}{31250}.
 \tag{39}
\]
The square of this last number is strictly greater than
\(273/400\), since
\[
 400\cdot25871^2=267723456400
                >266601562500=273\cdot31250^2.
 \tag{40}
\]
This contradicts (38). The supposition \(K\ge7/10\)
is impossible, proving (5).

Every comparison above concerns the same actual positive
logarithmic solution. The two-sine endpoint condition, the
cosine modulus bounds, and the distinguished cubic sheet
were fixed before the inequalities were applied. No new
stationary solution, source asymptotic, or contour homology
is inferred by the squarings used to compare positive numbers.
The result places that already specified geometric point
inside the taller inner domain; controlling its outer closing
cycle remains an additional finite-source problem.

## Frozen source bindings

- Actual positive point, exact middle and cubic identities, and
  the initial angle/height box:
  0071c0fcb46fae09a0223f5c33542ff5424896a9c8eb3431dec9f378c4b3253f.
- Original unsquared closing system and geometric sheet:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Original lower height and unsquared Chebyshev deduction:
  c12acffe796dae3ad3e7990cd302020a7ff289e75f2e5c8b997836aa826764d3.
