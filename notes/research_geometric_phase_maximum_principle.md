# A maximum principle for the geometric cosine phases

Research note, 3 November 2026. Frozen manuscripts and running certificate
inputs are unchanged.

The cosine phases of a positive path satisfy a simple maximum principle.
It gives a short proof of the spectral half-plane bound and, more
usefully for pair activation, an upper bound for each real angle in
terms of its own charge. The latter removes a large part of the
parameter region considered in the existing support tests.

The argument uses the already proved positive charge family and height
bound. It does not use the spectral half-plane theorem as an input.
Thus it provides an alternative proof of that theorem without changing
its current file or the inputs of any running verification.

## 1. The geometric equations

Use the finite positive paths of the
[fractional-charge theorem](research_positive_path_fractional_charge_cube.md):
all selected integer powers satisfy \(n_v\ge3\), all charges satisfy
\(0\le\chi_v\le1\), and at least one outside endpoint is complete.
At a positive-charge vertex write
\[
 t_v=a_v-iH_v,\qquad 0<a_v<\pi,\qquad
 0<H_v<H_*:=\frac{23}{20}.
 \tag{1}
\]
Zero-charge vertices and complete outside endpoints have \(t_v=0\).
For an incidence \(vw\), its return on the original geometric branch is
\[
 r_{vw}=k_{vw}+ig_{vw}
   =\operatorname{arsinh}\!\left(
          \tan(t_v/2)\cos(t_w/2)\right).
 \tag{2}
\]
At an active vertex \(k_{vw}>0\). Its two real period equations are
\[
 \sum_{w\sim v}k_{vw}=\frac{n_vH_v}{2},\qquad
 \sum_{w\sim v}g_{vw}=\frac{n_va_v}{2}-\pi\chi_v .
 \tag{3}
\]
The sums have the original incidence degrees; an absent edge contributes
nothing. The branch in (2) has positive real part and imaginary part
in \((-\pi/2,\pi/2)\).

Put
\[
 B_v=\frac{\sinh H_v}{\sin a_v},\qquad
 \beta_v=\arg\cos(t_v/2).
 \tag{4}
\]
For an active vertex both numbers are positive. Direct trigonometric
identities give
\[
 \arg\tan(t_v/2)=-\arctan B_v,\qquad
 \tan\beta_v
   =\tanh(H_v/2)\tan(a_v/2)
   =B_v\,\frac{1-\cos a_v}{1+\cosh H_v}<B_v.
 \tag{5}
\]
Set \(\beta_v=0\) at complete vertices.

We will use the elementary strict bound
\[
 \cosh H_*<\frac74.
 \tag{6}
\]
For completeness, the positive series for \(\cosh x\) gives
\[
 \cosh x\le1+\frac{x^2}{2}
       +\frac{x^4}{24(1-x^2/30)}
 \quad(0\le x<\sqrt{30}).
\]
At \(x=23/20\), the right side is \(31889123/18353600\),
whose difference from \(7/4\) is \(229677/18353600>0\).

## 2. The maximum cosine phase

**Theorem 1.** Throughout this charge family,
\[
 \tan^2\beta_v<\frac9{11}<\frac{100}{121}
 \quad\text{at every active vertex. In particular}\quad
 0<\beta_v<\frac{\pi}{4}.
 \tag{7}
\]

*Proof.* If there are no active vertices the assertion is vacuous.
Otherwise choose a vertex \(v\) where \(\beta_v\) is largest.
Every neighbor has
\[
 \beta_w\le\beta_v<\arctan B_v.
 \tag{8}
\]
Thus each product in (2) has strictly negative argument, while its
real part remains positive. The same sign holds for \(g_{vw}\):
indeed
\[
 \sinh(k+ig)=\sinh k\cos g+i\cosh k\sin g
\]
on the specified branch. The second period equation therefore gives
\[
 a_v<\frac{2\pi\chi_v}{n_v}\le\frac{2\pi}{3}.
 \tag{9}
\]
Consequently
\[
 \tan^2\beta_v
   =\tanh^2(H_v/2)\tan^2(a_v/2)
   <3\,\frac{\cosh H_*-1}{\cosh H_*+1}
   <3\,\frac{3}{11}=\frac9{11}.
 \tag{10}
\]
Every other cosine phase is at most this maximum. The final
comparison in (7) has exact difference \(1/121\). \(\square\)

The maximizer of the cosine phase need not maximize height or real
angle. No such additional assertion is used.

## 3. A local angle bound in terms of the charge

The maximum principle gives a bound at every vertex, not just at the
maximizer. Let
\[
 b=\frac{10}{11},\qquad
 m_b(B)=\frac{b-B}{1+bB},\qquad
 \kappa_b=\frac{\sqrt{1+b^2}-1}{\sqrt{1+b^2}+1}.
 \tag{11}
\]

**Theorem 2.** Every active vertex satisfies
\[
 a_v\le\frac{2\pi\chi_v}{n_v}+\kappa_b\sin a_v
       <\frac{2\pi\chi_v}{n_v}+\frac3{20}\sin a_v,
 \qquad
 a_v<\frac{40\pi}{17n_v}\chi_v.
 \tag{12}
\]

*Proof.* Fix \(v\), and write \(a,H,B,n,\chi\) for its data.
By (7), all neighboring phases are less than \(\arctan b\).
If \(B\ge b\), every return has nonpositive imaginary part, so
\(a\le2\pi\chi/n\), which implies (12).

Suppose \(0<B<b\). The argument \(\varphi\) of each product in
(2) is at most \(\arctan b-\arctan B\). If \(\varphi\le0\)
then \(g\le0\). If \(\varphi>0\), the same identity for
\(\sinh(k+ig)\) gives
\[
 \tan g=\tanh k\,\tan\varphi,\qquad
 g\le k\tan\varphi\le k\,m_b(B).
 \tag{13}
\]
Thus this last upper bound holds in both cases. Summing it and
using both equations (3) yields
\[
 a-\frac{2\pi\chi}{n}\le Hm_b(B)
 \le \sin a\,\frac{B(b-B)}{1+bB}.
 \tag{14}
\]
The second inequality uses \(H\le\sinh H=B\sin a\).
The maximum of \(B(b-B)/(1+bB)\) on \(0\le B\le b\)
is \(\kappa_b\). Differentiation gives its unique interior
maximizer \((\sqrt{1+b^2}-1)/b\).

For \(b=10/11\),
\[
 \kappa_b=\frac{\sqrt{221}-11}{\sqrt{221}+11}<\frac3{20},
 \quad\text{since}\quad
 221\cdot17^2=63869<64009=23^2\cdot11^2.
 \tag{15}
\]
This proves the first two bounds in (12). Finally \(\sin a\le a\)
gives \(17a/20<2\pi\chi/n\). \(\square\)

Using only \(\beta<\pi/4\), the same proof gives the weaker constant
\(3-2\sqrt2\) in place of \(3/20\). The rational refinement (15)
uses the quantitative maximum principle (7).

## 4. The spectral half-plane as a consequence

**Corollary 3.** Every geometric free color in the stated charge
family satisfies
\[
                         \Re(-2\cos t_v)<\frac74.
 \tag{16}
\]

*Proof.* Complete vertices give the value \(-2\). At an active
vertex with \(a\le2\pi/3\),
\[
 -2\cos a\cosh H\le\cosh H<\frac74.
 \tag{17}
\]
If \(a>2\pi/3\), the proof of Theorem 2 shows \(B<b\).
Since \(\sin a<\sqrt3/2\), (12) gives
\[
 a<\frac{2\pi}{3}+\frac{3\sqrt3}{40},
 \qquad
 \cos a>-\frac{49}{80}.
 \tag{18}
\]
The cosine estimate follows from
\(\cos(2\pi/3+u)\ge-1/2-\sqrt3\,u/2\).
Also
\[
 \sinh H=B\sin a<\frac{5\sqrt3}{11},
 \qquad \cosh H<\frac{14}{11}.
 \tag{19}
\]
Consequently
\[
             \Re(-2\cos t)<\frac{343}{220}<\frac74.
 \tag{20}
\]
This proves the assertion in both angle ranges. \(\square\)

This recovers the conclusion of the
[geometric half-plane theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_geometric_spectral_half_plane.md).
In particular, for \(N\ge16\), its physical Jacobi matrices obey
\[
 c_0-\Re w>\frac14-\frac{\pi^2}{N^2}>\frac15,
 \qquad \|(\mathcal J_j-wI)^{-1}\|\le5,
 \tag{21}
\]
with the same original boundary forcing and first-normal
qualifications as in the
[Jacobi boundary problem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_physical_jacobi_charge_boundary.md).

## 5. Reducing the pair-height search region

Consider the two power-three vertices in
[simultaneous pair activation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_positive_path_pair_activation_gap.md).
They have the same charge \(\chi\), and let \(H\) be their larger
height. If the scaled height estimate fails, then
\(\chi\le50H/59\). Theorem 2 applies to both vertices, even to
the one with smaller height, and gives
\[
             a_v,a_w<\frac{2000\pi}{3009}H
                         <\frac{209}{100}H .
 \tag{22}
\]
The last strict comparison follows already from \(\pi<22/7\).
For example, throughout \(H\le1/2\) both angles are less than
\(209/200\). This removes the large-angle part of the old
sector-only search region by an analytic argument.

More precisely, the angle at the maximum-height endpoint lies in
\[
 \arcsin\!\left(\frac{\sinh H}{\sqrt3}\right)
 \le a\le
 \min\left\{
   \pi-\arcsin\!\left(\frac{\sinh H}{\sqrt3}\right),
   \frac{2000\pi}{3009}H,
   \arccos\!\left(-\frac{7}{8\cosh H}\right)
 \right\}.
 \tag{23}
\]
The closed inequalities deliberately enlarge the strict geometric
domain. The first two sector bounds are existing results; the last
two are consequences of (22) and (16).

For the affine height estimate, put
\[
 \chi_{\max}(H)=
       \min\left\{1,\frac{40}{37}\left(H-\frac{37}{200}\right)\right\}.
 \tag{24}
\]
A failure of that estimate implies \(\chi\le\chi_{\max}(H)\).
In addition to the sector and spectral restrictions in (23),
Theorem 2 then gives the stronger implicit bound
\[
 a-\frac3{20}\sin a
       <\frac{2\pi}{3}\chi_{\max}(H).
 \tag{25}
\]
The function on the left is strictly increasing. Its unique inverse,
or any rigorously larger elementary bound, may therefore be used
to restrict a subsequent support verification.

The neighboring cosine domains can also be reduced: writing
\(c=x+iy=\cos(t_w/2)\), Theorem 1 and Corollary 3 give
\[
             0\le y\le\frac{10}{11}x,\qquad
                         x^2-y^2>\frac1{16}.
 \tag{26}
\]
The value \(c=1\) at a complete neighbor satisfies these conditions.
An absent incidence has return zero and must be included separately;
it is not represented by a cosine satisfying (26). Intersecting the
old cosine domains with (26) introduces new boundary pieces, so the
old arc-only support verification cannot be reused without checking
those pieces.

These are reductions of the domain containing the actual geometric
solution. They do not assert the old support inequalities at all
points of their larger rectangles. No running certificate has been
changed, and neither the full pair-height estimate nor the integrated
pair-energy gap follows until the remaining support bounds are proved.

## 6. A stronger angle restriction at larger heights

When \(\sinh H\ge b=10/11\), the signs in the local return equation
give a further reduction. Define
\[
 d(H)=\frac{\sinh H-b}{1+b\sinh H}\ge0.
 \tag{27}
\]

**Proposition 4.** At an active vertex of power \(n\), charge \(\chi\)
and height \(H\ge\operatorname{arsinh}b\),
\[
 a\le\frac{2\pi\chi}{n}
       -\frac2n\arctan\!\left(
                       d(H)\tanh\frac{nH}{2}\right).
 \tag{28}
\]
The following implicit bound is at least as strong:
\[
 a\le\frac{2\pi\chi}{n}
       -\frac2n\arctan\!\left[
       \frac{\sinh H-b\sin a}{\sin a+b\sinh H}
                       \tanh\frac{nH}{2}\right].
 \tag{29}
\]

*Proof.* Since \(B=\sinh H/\sin a\ge\sinh H\ge b\), every
product in (2) has nonpositive argument. In fact, its argument
\(\varphi\) satisfies
\[
 -\varphi\ge\arctan B-\arctan b,\qquad
 \tan(-\varphi)\ge d_B:=\frac{B-b}{1+bB}\ge d(H).
 \tag{30}
\]
Here \(0\le-\varphi<\pi/2\). The identity used in (13), with
the opposite sign, therefore gives
\[
 -g\ge f_{d_B}(k),\qquad
                  f_d(k):=\arctan(d\tanh k).
 \tag{31}
\]
For \(d\ge0\), this is an increasing concave function on
\([0,\infty)\), with \(f_d(0)=0\). Directly,
\[
 f_d''(k)=
 -\frac{2d(1+d^2)\tanh k\,\operatorname{sech}^2k}
              {(1+d^2\tanh^2k)^2}\le0.
 \tag{32}
\]
For any nonnegative \(k_i\) with sum \(S\), concavity gives
\(f_d(k_i)\ge(k_i/S)f_d(S)\) when \(S>0\). Consequently
\[
 \sum_i(-g_i)\ge f_{d_B}\!\left(\sum_i k_i\right)
     \ge f_{d(H)}(nH/2).
 \tag{33}
\]
Insert the imaginary period equation (3) to obtain (28).
Keeping \(d_B=(\sinh H-b\sin a)/(\sin a+b\sinh H)\) gives
(29). An absent incidence contributes zero to both sums, so the
same argument applies to terminal vertices. \(\square\)

The whole affine search range has \(H\ge37/40>10/11\), hence
\(\sinh H>b\). A failure of the affine height estimate must therefore
satisfy, at its maximum-height endpoint,
\[
 a\le\frac{2\pi}{3}\chi_{\max}(H)
       -\frac23\arctan\!\left(d(H)\tanh\frac{3H}{2}\right),
 \tag{34}
\]
in addition to the earlier restrictions. The explicit right side
is a rigorous bound; using the stronger implicit inequality (29)
would require retaining its dependence on \(a\) in the verifier.
Neither inequality estimates the real return sum by itself. They
reduce the parameter domain of the remaining support problem and
do not replace that problem by a claimed height theorem.

## 7. A sharper bound for the maximum cosine phase

The negative return phases at a maximizing vertex give more than their
sign. Retaining their sizes improves (7) to a bound that removes
some of the largest possible neighboring returns.

**Theorem 5.** Throughout the positive charge family of Section 1,
\[
                         \tan^2\beta_v<\frac12.
 \tag{35}
\]

*Proof.* Choose a vertex attaining the positive maximum of \(\beta\),
and omit its subscript. Put
\[
 \tau=\tanh(H/2),\qquad b_*=\tan\beta,\qquad
 q=\tau^2,\qquad B_*=b_*^2.
 \tag{36}
\]
The letters \(B_*,b_*\) in this proof denote squared phase and phase,
not the return ratio \(B=\sinh H/\sin a\) from (4).
Equation (5) gives \(b_*=\tau\tan(a/2)\).
Because every neighboring cosine phase is at most \(\beta\),
the negative argument of each product in (2) is at least
\(\arctan B-\beta\). Its tangent simplifies exactly:
\[
 \tan(\arctan B-\beta)
   =\frac{B-b_*}{1+Bb_*}
   =\tanh(H/2)\cot(a/2)=\frac{\tau^2}{b_*}.
 \tag{37}
\]
Apply the concavity argument (31)--(33), now with
\(d=\tau^2/b_*\), to all incidences at this vertex. Both period
equations give
\[
 \frac{na}{2}
   +\arctan\!\left(\frac{\tau^2}{b_*}\tanh\frac{nH}{2}\right)
       \le\pi\chi\le\pi.
 \tag{38}
\]
The left side increases with \(n>0\). Since \(n\ge3\), the
triple-angle identity for the hyperbolic tangent yields
\[
 3\arctan(b_*/\tau)
 +\arctan\!\left(
       \frac{\tau^3(3+\tau^2)}{b_*(1+3\tau^2)}\right)\le\pi.
 \tag{39}
\]

Suppose \(B_*\ge1/2\). The previous maximum principle and
(6) give
\[
 \frac{B_*}{3}\le q<\frac3{11},\qquad
                       \frac12\le B_*<\frac9{11}<1.
 \tag{40}
\]
The first inequality follows from \(a<2\pi/3\). In particular
\(3\arctan(b_*/\tau)\) lies in \((\pi/2,\pi]\).
The other angle in (39) is positive and less than \(\pi/2\).
Consequently (39) is equivalent to the tangent inequality
\[
 \frac{\tau^3(3+\tau^2)}{b_*(1+3\tau^2)}
       \le
 \frac{b_*(3\tau^2-b_*^2)}
                 {\tau(3b_*^2-\tau^2)}.
 \tag{41}
\]
All denominators are positive on (40). Multiplying out, (41)
requires
\[
 \begin{split}
 P(q,B_*):={}&q^4+3(1-B_*)q^3
                   +3B_*(1-B_*)q-B_*^2\ge0.
 \end{split}
 \tag{42}
\]
This polynomial is strictly increasing in \(q>0\) for
\(0<B_*<1\), and strictly decreasing in \(B_*\ge1/2\):
\[
 \begin{split}
 P_q&=4q^3+9(1-B_*)q^2+3B_*(1-B_*)>0,\\
 P_{B_*}&=-3q^3+3(1-2B_*)q-2B_*<0.
 \end{split}
 \tag{43}
\]
But
\[
 P(q,B_*)\le P(3/11,1/2)=-\frac{139}{14641}<0,
 \tag{44}
\]
contradicting (42). The maximal phase therefore satisfies (35),
as do all other phases. \(\square\)

The proof also covers a terminal vertex: it uses the actual sum of
returns, and concavity is valid for one or more nonnegative terms.
No assumption that the two returns have equal real parts is made.

Theorem 2 can now be applied with \(b=1/\sqrt2\). Its optimal
constant is
\[
 \kappa_b=\frac{\sqrt6-2}{\sqrt6+2}<\frac19,
 \tag{45}
\]
where the strict comparison is \(8\sqrt6<20\).
Thus every positive vertex satisfies
\[
 a<\frac{2\pi\chi}{n}+\frac19\sin a,\qquad
                         a<\frac{9\pi}{4n}\chi.
 \tag{46}
\]
For a failed scaled pair estimate this gives the particularly simple
restriction
\[
                       a_v,a_w<\frac{75\pi}{118}H<2H.
 \tag{47}
\]
Here \(75(22/7)/118=825/413<2\).
Proposition 4 likewise holds with \(b=1/\sqrt2\).

For later support estimates, the neighboring cosine now lies in
the quarter ellipse (5) intersected with
\[
                            0\le y\le x/\sqrt2.
 \tag{48}
\]
This conclusion is independent of the current support certificates.
It is a stronger restriction on the actual geometric solution, not
an assertion that the previous support inequalities hold throughout
their larger domains.

## 8. A single arc suffices for the smaller cosine domain

For a height cap \(C>0\), let \(D_C\) be the quarter ellipse
from the pair-activation note, and put
\[
 D_C^\sharp=D_C\cap\{x+iy:0\le y\le x/\sqrt2\},\qquad
 \vartheta_C=\arctan\!\left(\frac1{\sqrt2}\coth(C/2)\right).
 \tag{49}
\]
Theorem 5 puts every neighboring geometric cosine in this domain.
The complete cosine \(1\) and the zero return used for an absent
incidence are included.

**Proposition 6.** Fix \(A=\tan((a-iH)/2)\) with
\(0<a<\pi\), \(H>0\), and a real support slope \(s\le0\).
Then
\[
 \begin{split}
 &\max_{c\in D_C^\sharp}
       \{\Re\operatorname{arsinh}(Ac)
                         -s\Im\operatorname{arsinh}(Ac)\}\\
 &\quad=
 \max\left\{0,\
   \max_{0\le\vartheta\le\vartheta_C}
      \left[\Re\operatorname{arsinh}(Ac_C(\vartheta))
                    -s\Im\operatorname{arsinh}(Ac_C(\vartheta))\right]
       \right\},\\
 &\hspace{30mm}
 c_C(\vartheta)=\cosh(C/2)\cos\vartheta
                         +i\sinh(C/2)\sin\vartheta .
 \end{split}
 \tag{50}
\]
All branches are the original right-half-plane branches.

*Proof.* The domain is star-shaped about zero. On any ray
\(c=r e^{i\beta}\) in the domain, write
\(\varphi=\arg(Ae^{i\beta})\). It lies strictly between
\(-\pi/2\) and \(\pi/2\). Apart from a positive real factor,
the radial derivative of the support function has argument
\[
 \arctan s+\delta(r),\qquad
 \delta(r)=\varphi-\frac12\arg(1+r^2A^2e^{2i\beta}).
 \tag{51}
\]
If \(\varphi\ge0\), then \(0\le\delta(r)\le\varphi\), so
this derivative has positive real part. If \(\varphi<0\),
\(\delta(r)\) increases from \(\varphi\) toward zero:
its derivative is
\(-r\Im(A^2e^{2i\beta})/|1+r^2A^2e^{2i\beta}|^2>0\).
The angle in (51) stays in \((-\pi,0]\). Its cosine can
therefore change sign only from negative to positive.
The support function on the ray has no strict interior maximum;
its maximum is at zero or at the outer endpoint.

The outer endpoints form precisely the ellipse arc in (50).
The relation \(y/x\le1/\sqrt2\) is equivalent there to
\(\vartheta\le\vartheta_C\). Taking the maximum over rays proves
the formula. \(\square\)

Thus both support terms for pair activation can be bounded using one
arc and the value zero, even in the affine regime. The old
three-piece sector boundary need not be retained if this smaller
phase domain is used instead. This observation gives a simpler
candidate for a new verification; it does not certify its support
inequalities by itself.
