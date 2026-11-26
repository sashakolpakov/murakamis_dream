# Original wire-cut guards beyond the inner right half-angle

Private source-domain deduction, 9 November 2026. The selected outer
charged curve has an additional angle-height correlation. It supplies
strict original factorial-cut bounds for the second shortened edge
when the first angle moves from \(\pi/2\) to \(2\pi/3\). On the
actual first-height range, the real wire profile also has no local
minimum. These are ingredients for a finite contour construction,
not a completed edge packet or an estimate for the inner right current.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Actual selected-sheet correlations

Let \(u_\delta=\beta-iK\) be the original selected curve in
[the full-interval phase theorem](research_mixed_next_selected_charged_curve_full_interval.md),
\(0\le\delta\le1/2\). Write
\(c_*(u)=\cos(t_*(u)/2)\). For positive \(\delta\), its proved
guards and exact critical equation are
\[
\begin{gathered}
 0<\beta<4/3,\quad0<K<1/2,\quad |c_*|<1,\\
 \operatorname{arsinh}\{c_*(u)\tan(u/2)\}
                  =i(3u/2-\pi\delta).
\end{gathered}
\tag{1}
\]
All inverse functions have the original principal logarithmic lift.

**Lemma 1.** On this actual curve,
\[
 K<\beta/2,\qquad
 |\cos u|<1,\qquad
 \Re\cos u>7/30,\qquad \Im\cos u>0
                       \quad(\delta>0).
\tag{2}
\]
At \(\delta=0\), \(u=0\); the weak modulus bound and the real
lower bound remain valid.

*Proof.* Suppose \(\beta\le2K\). Then \(\beta\le1\), and
on the segment from zero to \(u/2\),
\[
 |\cos(su/2)|^2\ge\cos^2(1/2)>(7/8)^2.
\]
Integration of the tangent derivative gives
\[
 |\tan(u/2)|\le\frac{32}{49}|u|
       \le\frac{32\sqrt5}{49}K<\frac{72}{49}K<\frac32K.
\tag{3}
\]
Here \(\sqrt5<9/4\). For \(z\) in the right half-plane,
\(\Re\operatorname{arsinh}z\le\operatorname{arsinh}|z|\le|z|\).
The argument in (1) is in that half-plane by the original guards.
Thus (3), \(|c_*|<1\), and the real part of (1) contradict
\(\Re\operatorname{arsinh}=3K/2\). This proves the first assertion.

For \(0<K<1/2\), the positive series gives
\[
 \sinh K\le\frac{K}{1-K^2/6}<\frac{24K}{23}
          <\frac{12\beta}{23},
 \qquad
 \sin\beta\ge\beta-\beta^3/6>\frac{19\beta}{27}.
\tag{4}
\]
Since \(12/23<19/27\), one has \(\sinh K<\sin\beta\).
Consequently
\(|\cos u|^2=\cos^2\beta+\sinh^2K<1\).
The rational cosine bound in the phase theorem gives
\(\cos(4/3)>7/30\), so
\(\Re\cos u=\cos\beta\cosh K>7/30\).
The imaginary part is \(\sin\beta\sinh K>0\).
\(\square\)

The actual inner critical height satisfies the stronger bound
\[
                         2/3<H(u_\delta)<1.
\tag{5}
\]
Indeed write \(v=2c_*=x+ib\) in the original cubic. Its imaginary
equation is
\[
 (3b-2)x^2-b^3+2b^2-3b+2=2\Im\cos(u/2)\ge0.
\tag{6}
\]
The left side increases in \(b\in[1/3,2/3]\), since
\(x>3/2\). At \(b=1/2\) it is
\(-x^2/2+7/8<-1/4\). Hence \(b>1/2\).
As in [the original complete-height proof, (5)--(7)](research_inner_three_complete_action_upper_bound.md),
\(b=2\sin(\Re t_*/2)\sinh(H/2)<\sqrt2\sinh(H/2)\).
If \(H\le2/3\), the written bounds
\(\sqrt2<10/7\), \(\sinh(1/3)<18/53\) would give
\(b<180/371<1/2\), a contradiction. The original cubic
theorem supplies \(H<1\).

## 2. The enlarged first-angle family and its exact force

For the rest of the note let
\[
 t=a-iH,\qquad \pi/2\le a\le2\pi/3,\qquad2/3\le H\le1,
 \qquad u=u_\delta,\quad0\le\delta\le1/2.
\tag{7}
\]
In particular this includes the original first horizontal at
height \(H(u_\delta)\). Retain the literal edge
\[
 K_N^<(t,u)=\sum_{j=0}^{\lfloor N/2\rfloor-1}
                       e_j(-2\cos t)e_j(-2\cos u).
\tag{8}
\]
For its original factorial wire variable \(y\), the zero-safe
upper exponent is \(\mathcal V=\mathfrak b(y,t)+\mathfrak b(y,u)\).
Away from its zeros and cuts its horizontal force modulus is
\[
 \mathfrak f(y)=
 \left|\frac{(\cos(2\pi y)+\cos t)(\cos(2\pi y)+\cos u)}
                    {(1-\cos(2\pi y))^2}\right|.
\tag{9}
\]
This is \(|e^{F_y}|\) for the original phase \(F=b(y,t)+b(y,u)\),
with its zero logarithmic charge. The original shifted factorials
give upper cuts
\[
 y=x+iH/(2\pi),\quad x\ge\tfrac12-a/(2\pi),
 \qquad
 y=x+iK/(2\pi),\quad x\ge\tfrac12-\beta/(2\pi),
\tag{10}
\]
within \(0<x\le1/2\). They are exactly the cuts in
[the mixed-height edge proof, (8)--(14)](research_mixed_next_shortened_edge_mixed_height_packet.md).
At \(u=0\) the second has no interior segment.

**Lemma 2.** Throughout (7), both cuts in (10) have a fixed strict
force bound:
\[
 \mathfrak f\le\sqrt{23/24}<1\quad\hbox{on the first cut},
 \qquad
 \mathfrak f\le\frac{13\sqrt{79}}{150}<1
                                  \quad\hbox{on the second cut}.
\tag{11}
\]
These include cut intersections and starting zeros by continuity.

*Proof on the first cut.* Put
\[
 C=\cosh H,\quad S=\sinh H,\quad d=\cos a\in[-1/2,0],
 \quad q=-\cos(2\pi x)\in[d,1],\quad s_q=\sqrt{1-q^2}.
\]
Then \(1\le C<8/5\), and
\[
 \cos(2\pi y)=-Cq-iSs_q,\qquad
 |1-\cos(2\pi y)|=C+q\ge1/2.
\tag{12}
\]
The square of the first numerator is
\[
 O=C^2(q-d)^2+(C^2-1)(s_q-\sqrt{1-d^2})^2.
\tag{13}
\]
For fixed \(q,C\), this increases as \(a\) increases through
its eligible range. In fact its derivative divided by two is
\[
 C^2(q-d)\sin a+(C^2-1)(\sin a-s_q)d.
\]
For \(q\le0\), one has \(d\le q\le0\), so the second
term is nonnegative. For \(q\ge0\), it is either nonnegative
or bounded below by \((C^2-1)\sin a\,d\); in the latter case
the sum is at least \(\sin a(C^2q-d)>0\).
Thus (13) is bounded by its value at \(d=-1/2\).

First suppose \(-1/2\le q\le0\). Lemma 1 gives, writing
\(\cos u=P+iQ\),
\(P\le1\), \(Q\ge0\), and \(|\cos u|\le1\). Therefore
\[
 |\cos(2\pi y)+\cos u|^2
       \le|\cos(2\pi y)+1|^2=(C-q)^2.
\tag{14}
\]
Indeed the difference of the squares is
\(|\cos u|^2-1-2Cq(P-1)-2Ss_qQ\le0\).
Also
\[
 s_q-\sqrt3/2
   =\frac{(1/2-q)(1/2+q)}{s_q+\sqrt3/2},
\]
so (13) is at most
\((q+1/2)^2(4C^2-1)/3\). Put \(v=-q\in[0,1/2]\).
Equations (9),(12),(14) now give
\[
 \mathfrak f
 \le\frac{2}{\sqrt3}
       \frac{C(1/2-v)(C+v)}{(C-v)^2}
 \le\frac{2}{\sqrt3}
       \frac{(1/2-v)(1+v)}{(1-v)^2}
 \le\frac9{8\sqrt3}.
\tag{15}
\]
The middle expression decreases with \(C\ge1\): the logarithmic
derivative of \(C(C+v)/(C-v)^2\) has numerator
\(-v^2-3Cv\le0\). The last inequality is precisely
\((1-5v)^2\ge0\) after clearing denominators. Its squared
bound \(27/64\) is less than \(23/24\).

For \(0\le q\le1\), use
\(\sqrt3\sqrt{1-q^2}\ge(5/3)(1-q)\) in (13). It gives
\[
 O\le q^2+A_Cq+B_C,\quad
 A_C=\frac{8C^2-5}{3},\quad B_C=\frac{4C^2-1}{12}.
\tag{16}
\]
Lemma 1 and \(P>7/30,Q\ge0\) give for the second numerator
\[
 |\cos(2\pi y)+\cos u|^2
           \le C^2+q^2-\frac7{15}Cq.
\tag{17}
\]
Write \(d_0=7/15\). The denominator minus the product of the
two upper numerators is the polynomial
\[
\begin{split}
 &(C+q)^4-(q^2+A_Cq+B_C)(q^2-d_0Cq+C^2)\\
 &=[(4+d_0)C-A_C]q^3
    +[5C^2-B_C+d_0CA_C]q^2\\
 &\hspace{8mm}+[C^2(4C-A_C)+d_0CB_C]q
    +C^2(C^2-B_C).
\end{split}
\tag{18}
\]
All four coefficients are positive for \(1\le C\le8/5\).
For the first and the factor in the third, concavity in \(C\)
reduces to the two endpoints and gives
\[
 (4+d_0)C-A_C\ge149/75>0,
 \qquad 4C-A_C\ge31/25>0.
\]
The others are positive since \(A_C,B_C>0\) and
\(B_C<C^2/3\). In particular (18) is greater than
\(2C^4/3\), while \((C+q)^4\le16C^4\).
Thus the squared force is at most \(23/24\), proving
the first part of (11).

*Proof on the second cut.* Its own real angle is
\(\beta<4/3<\pi/2\), so the original nonnegative-cut-coordinate
calculation in the mixed-height proof is eligible. Its height has
\(\cosh K<8/7\), and the other leg satisfies
\(|\cos t|\le\cosh H<8/5\). Equations (10)--(12) of that proof
therefore give exactly \(13\sqrt{79}/150\). Its square is
\(13351/22500<1\). No part of the earlier first-cut formula with
a negative cut coordinate has been imported. \(\square\)

## 3. The actual critical sheet and the real wire profile

Put
\[
 A=\cos^2(t/2),\quad B=\cos^2(u/2),\quad
 D_0=A+B-AB,\quad W=AB/D_0.
\tag{19}
\]
The family (7) satisfies
\[
 \Re A>1/10,\quad |A|<4/5,\quad
 \Re B>37/60,\quad |B|\le1,
 \quad \Re(1/B)\ge1,
\tag{20}
\]
where the last two equalities are possible only at \(u=0\).
Indeed \(\Re A=(1+C\cos a)/2\), \(|A|=(C+\cos a)/2\),
and \(|\cos u|\le1\) implies \(|B|^2\le\Re B\).
Also
\[
 |1-A|<21/20,\qquad |1-B|<9/20,
 \qquad |1-D_0|<189/400,
\]
using \(\cosh K<17/15\), \(\cos\beta>7/30\).
Consequently
\[
 \Re D_0>211/400,\qquad
 \Re(1/W)=\Re(1/A)+\Re(1/B)-1>5/32.
\tag{21}
\]
The last estimate uses \(\Re A>1/10\) and \(|A|^2<16/25\).
All quantities stay in fixed compact eligible domains.

The principal saddle \(y_*=\pi^{-1}\arctan\sqrt W\) remains
in \(0<\Re y_*<1/2\). The original force identity
\[
 e^{F_y}-1
     =-\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},
                 \qquad z_y=\tan\pi y,
\tag{22}
\]
has just this finite root in that strip. Start at \(a=\pi/2\)
and the actual height \(H(u)\), where the adopted positive/mixed-height
packet fixes the zero logarithmic charge. First vary \(H\) within
\([2/3,1]\) at \(a=\pi/2\), then vary \(a\) to its desired
value. All these paths satisfy the guards just proved. Lemma 2
prevents the root from crossing any original cut or zero. Thus the
original equalities continue:
\[
 F_y(y_*)=0,\qquad F(y_*)=\psi(t,u),\qquad
 -F_{yy}(y_*)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0.
\tag{23}
\]
These are phase identities with their original constants, not yet
a finite packet on the enlarged domain.

For the real wire, set \(v=\sin^2\pi x\), \(0<x<1/2\),
and \(q_A=|A-v|/v\), \(q_B=|B-v|/v\). The original horizontal
derivative is \(\partial_x\mathcal V=\log(q_Aq_B)\), and
\[
 \partial_v\log q_A
   =\frac{\Re A\,v-|A|^2}{v|A-v|^2},
\tag{24}
\]
with the same formula for \(B\), away from numerator zeros.

For this family,
\[
       |A|^2/\Re A>1/2,\qquad |B|^2/\Re B>1/2.
\tag{25}
\]
For the first, \(C=\cosh H>11/9\) and \(d=\cos a\in[-1/2,0]\).
The required inequality is
\(C^2+Cd+d^2-1>0\); its minimum occurs at \(d=-1/2\),
then at \(C=11/9\), giving \(43/324>0\).
For the second the same numerator is
\(C_K^2+C_K\cos\beta+\cos^2\beta-1>0\), since
\(C_K\ge1\) and \(\cos\beta>0\).

If the first derivative in (24) is nonnegative, then
\(v>1/2\) and \(q_A^2\le1-\Re A/v<1\). Since
\(|B|^2\le\Re B\), one also has
\(q_B^2\le1+\Re B(1-2v)/v^2<1\).
Thus \(q_Aq_B<1\).

If the \(B\) derivative is nonnegative, then again \(v>1/2\),
and \(q_B^2\le1-\Re B/v<23/60\). On \(v\in[1/2,1]\)
one has the uniform bound
\[
                              q_A^2\le181/100.
\tag{26}
\]
To check it, put \(w=1/v\in[1,2]\). The exact expression
\(q_A^2=1-(1+Cd)w+(C+d)^2w^2/4\) is convex in
\(d\in[-1/2,0]\). At \(d=0\), its maximum is at most
\(39/25\); at \(d=-1/2\), increasing \(C\) to \(8/5\)
gives \(1-w/5+121w^2/400\le181/100\).
Both endpoint maxima follow by convexity in \(w\).
Thus in this second case
\((q_Aq_B)^2<4163/6000<1\) as well.

Whenever the real force is at least one, therefore, both derivatives
in (24) are strictly negative. The force starts at infinity and
ends at
\(|1-A||1-B|<189/400<1\). It crosses one exactly once,
downwards. Numerator zeros have zero force and do not add a crossing.
The real profile increases to one maximum and then decreases;
in particular it has no interior local minimum.

## 4. The finite-source estimate still required

Lemmas 1--2 and (19)--(26) supply actual selected-sheet guards
beyond the earlier first-angle restriction \(a\le\pi/2\).
They retain the complete two-leg force, both factorial cuts and
the original logarithmic branch. The cutoff and finite source in
(8) have not been changed.

They do not prove the endpoint-action inequality
\(\Re\psi(t,u)>(H+K)/2\) on the enlarged family, a contributing
joined contour with all endpoint/alias gaps, or the resulting finite
upper bound. Those require separate estimates. In particular no
bound for the off-grid right-middle current or for its outer Fourier
observation is inferred from the absence of cut or real-boundary
minima alone.

## Frozen source versions

- Global selected charged curve: `6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c`.
- Original cubic branch: `8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a`.
- Original mixed-height edge and force/cut identities: `fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07`.
- Original complete-height argument: `7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d`.
