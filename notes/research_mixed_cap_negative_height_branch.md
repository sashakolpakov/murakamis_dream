# The original cap critical branch at negative incoming height

Research deduction, 7 November 2026. The original cap critical
branch continues across the full incoming rectangle proposed
for the displaced contour. Both its private and auxiliary
critical coordinates stay in their original primitive chambers.
The critical equations retain their zero logarithmic lifts,
and the two critical points remain nondegenerate.

This supplies the cap phase on the same incoming domain as the
conditional phase. It does not place the private coordinate in
a particular endpoint-coefficient rectangle or prove a complete
finite cap asymptotic there. No numerical evaluation is used.

## 1. The marked phases and algebraic equations

At complete ordinary color retain
\[
\begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\\
 \Psi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea.
\end{split}
\tag{1}
\]
The primitives and additive constants are those of
[the original incoming continuation](research_mixed_half_face_general_incoming_transport.md).
Set
\[
 X=e^{-2\pi ia},\qquad \omega=e^{2\pi iu},\qquad p=e^{2\pi ie}.
\tag{2}
\]
The original endpoint relation and cap critical equation give
\[
\begin{split}
 p&=\frac{5\omega^2-2\omega+1}{(\omega+1)^2},\\
 f_X(\omega)&=(6-X)\omega^3-(5+2X)\omega^2+(4-X)\omega-1=0,\\
 p&=\frac{\omega(1-X)}{1-\omega},\qquad
                     X=1+p-p/\omega.
\end{split}
\tag{3}
\]
All equations refer to the branch selected at \(a=1/2\)
by the complete half-cap theorem.

Throughout this note
\[
 1/2\le\Re a\le7/10,\qquad -9/125\le\Im a\le0.
\tag{4}
\]
As proved in the
[conditional negative-height theorem](research_mixed_conditional_negative_height_branch.md),
these parameters satisfy
\[
 \Re X<0,\quad \Im X\ge0,\qquad 1/3<|X|^2\le1.
\tag{5}
\]
The strict lower bound follows from
\(e^{-36\pi/125}>e^{-1}>1/3\).

## 2. The selected roots remain in the upper half-plane

The discriminant of \(f_X\) is
\[
                       64(X^3-17X^2+19X-7).
\tag{6}
\]
Write \(X=c+ib\). If \(b>0\), the imaginary part of
the cubic factor in (6) is
\[
                      b(3c^2-b^2-34c+19)>0,
\tag{7}
\]
since \(c<0\) and \(b^2\le1\). If \(X<0\) is real,
that cubic factor is strictly negative. Thus all roots of
\(f_X\) are simple throughout (4). Its leading coefficient
never vanishes.

The parameter rectangle is contractible. Analytic continuation
from \(a=1/2\), first vertically and then horizontally,
defines the selected simple root throughout it, with a
holomorphic continuation to a fixed neighborhood. Equivalently
one can use the triviality of the simple-root covering over
this rectangle; no monodromy choice is being made along a loop.

The values \(\omega=0,-1,1\) are excluded by (3) and (5).
If \(\omega\) were real at a nonreal \(X\), rearrangement gives
\[
 X=\frac{6\omega^3-5\omega^2+4\omega-1}
                              {\omega(\omega+1)^2},
\tag{8}
\]
which is real. Along negative real \(X\), the negative
discriminant keeps the selected nonreal conjugate root
strictly above the real axis. Hence \(\Im\omega>0\)
throughout (4).

We also need \(\Im p>0\), not just \(\Im\omega>0\).
Suppose \(p\) is real. The endpoint quadratic is
\[
                  (p-5)\omega^2+2(p+1)\omega+p-1=0.
\tag{9}
\]
For \(p\ge1/2\), its roots are real, including its linear
degeneracy at \(p=5\), contrary to \(\Im\omega>0\).
For \(p<1/2\), its nonreal conjugate roots obey
\[
 |\omega|^2=\frac{1-p}{5-p},\qquad
             \Re\omega=\frac{p+1}{5-p}.
\tag{10}
\]
The last identity of (3) consequently gives
\[
 |X|^2=1-\frac{4p^3}{1-p},\qquad
                \Re X=\frac{(1+p)(1-2p)}{1-p}.
\tag{11}
\]
If \(p<0\), the first contradicts \(|X|\le1\).
If \(0\le p<1/2\), the second contradicts \(\Re X<0\).
Thus \(p\) never reaches the real axis. Its initial imaginary
part is positive, so \(\Im p>0\) throughout (4).

Choose \(\Log p,\Log\omega\) with arguments in \((0,\pi)\).
Their logarithmic coordinates \(e,u\) are then continuous
and holomorphic near the compact parameter set.

## 3. The incoming numerator wall

We show that \(p\) cannot lie on the positive ray through \(X\).
At negative real \(X\) this follows from \(\Im p>0\).
Otherwise suppose \(p=sX\), \(s>0\). Eliminating \(\omega\)
from (3) gives
\[
 4p^2(p-X)+(1-X)^2(p-1)=0.
\tag{12}
\]
Thus \(X\) would be a nonreal root of the real polynomial
\[
 A_sX^3-(2s+1)X^2+(s+2)X-1=0,\qquad
                         A_s=s(2s-1)^2.
\tag{13}
\]
If \(s=1/2\), this is
\(-2X^2+(5/2)X-1=0\); its nonreal roots have real part
\(5/8>0\). Hence \(A_s>0\).

The roots of (13) are \(X,\bar X,\alpha\), where \(\alpha\)
is real. Put \(R=|X|^2\) and \(c=\Re X<0\).
Vieta's product, sum and pair relations give
\[
 \alpha=\frac1{A_sR}>0,\qquad
 \frac1R+2A_sc=2s+1,\qquad
                       A_sR+\frac{2c}{R}=s+2.
\tag{14}
\]
The middle equation and \(R>1/3\) imply \(2s+1<3\),
so \(0<s<1\). But then \(A_s<s\), and \(R\le1\)
gives \(A_sR<s\), contrary to the last equation,
which requires \(A_sR>s+2\). This excludes (13).

At \(\Re a=1/2\), \(\arg p<\arg X=\pi\).
The ray exclusion preserves that strict ordering. Hence
\[
                         0<\Re e<1-\Re a.
\tag{15}
\]

## 4. The private-minus-auxiliary wall

The remaining chamber condition is \(\Re u<\Re e\).
Suppose to the contrary that \(p=s\omega\), \(s>0\),
at a first crossing of the corresponding ray.
The endpoint equation (9) becomes the real cubic
\[
 f_s(\omega)=s\omega^3+(2s-5)\omega^2+(s+2)\omega-1=0.
\tag{16}
\]
Its roots are \(\omega,\bar\omega,\alpha\), with \(\alpha>0\).
The relation \(X=1-s+s\omega\) and Vieta's formulas imply
\[
 \Re X=\frac72-2s-\frac{s\alpha}{2},
\qquad
 |X|^2=3(s-1)(s-2)
                      +s\left(\alpha(s-1)+\frac1\alpha\right).
\tag{17}
\]
For the second equality, use
\(\alpha|\omega|^2=1/s\) and
\(2\Re\omega+\alpha=(5-2s)/s\) when expanding
\(|1-s+s\omega|^2\).

If \(0<s\le3/2\), put \(b_s=(7-4s)/s>0\).
A direct polynomial calculation gives
\[
 f_s(b_s)=\frac{98}{s^2}-\frac{196}{s}+142-36s.
\tag{18}
\]
This is strictly positive. For \(s\le1\), write it as
\(98(s^{-1}-1)^2+44-36s\).
For \(1\le s\le3/2\), put \(z=s-1\in[0,1/2]\);
then
\[
 s^2f_s(b_s)=8-20z+34z^2-36z^3
                     \ge8-20z+16z^2>0.
\tag{19}
\]
The final quadratic has negative discriminant and positive
leading coefficient. Since
\(f_s(b_s)=s(b_s-\alpha)|b_s-\omega|^2\),
it follows that \(\alpha<b_s\). The first equation in
(17) would therefore give \(\Re X>0\), a contradiction.

If \(s\ge3/2\), the arithmetic-geometric mean inequality in
the second equation of (17) gives
\[
 |X|^2
 \ge3(s-1)(s-2)+2s\sqrt{s-1}
 \ge-\frac34+\frac3{\sqrt2}>1.
\tag{20}
\]
This contradicts \(|X|\le1\). Both possibilities have
been excluded.

At the original half face \(0<\arg\omega<\arg p<\pi\).
Neither argument leaves this interval, and their difference
cannot vanish by the ray exclusion. Consequently
\[
                          0<\Re u<\Re e.
\tag{21}
\]
This argument did not assume that \(|p|\ge1\) or that
the private height has either sign.

## 5. Original lifts and nondegeneracy

Equations (15), (21) put
\[
                   u,\quad 1/2-u,\quad e-u,\quad e+a,\quad a
\]
in their original open primitive strips. None meets a divisor.
The exponentiated stationary equations therefore retain their
original zero logarithmic lifts by continuation:
\[
                          F_u=0,\qquad \Psi_e=0.
\tag{22}
\]
In particular \(S(e)\) and the cap action
\(\mathcal T(a)=\Psi(e(a),a)\) have their original absolute
normalizations.

The endpoint discriminant \(16(2p-1)\) is nonzero for
upper-half-plane \(p\). Its selected critical point is
therefore nondegenerate. For the outer critical point,
the exact algebra in (3) gives
\[
 e^{\Psi_e}-1
       =\frac{f_X(\omega)}{(\omega+1)^2(p-\omega)}.
\tag{23}
\]
Also
\[
              \frac{dp}{d\omega}
                     =\frac{4(3\omega-1)}{(\omega+1)^3}\ne0.
\tag{24}
\]
At the selected root, differentiation of (23) with respect
to \(e\), at fixed \(a\), gives
\[
 \Psi_{ee}=
 \frac{f_X'(\omega)\,\omega_e}
      {(\omega+1)^2(p-\omega)},\qquad
 \omega_e=\frac{2\pi i\,p}{dp/d\omega}.
\tag{25}
\]
Every factor is nonzero: simplicity gives \(f_X'\ne0\);
the upper-half-plane and ray exclusions give all the other
nonvanishing statements. Thus \(\Psi_{ee}\ne0\).

Compactness now supplies positive margins from the listed
primitive divisors and a fixed complex neighborhood of (4)
for the continued original phase. Its incoming multiplier
still has the exact form
\[
 \exp\mathcal T_a=\left(\frac{k}{p}\right)^2,\qquad
                            k=\frac{1-\omega}{1+\omega},
\tag{26}
\]
by the original rational identity. No finite-source estimate
is inferred from this multiplier.

## 6. What remains for the complete cap

The [conditional branch theorem](research_mixed_conditional_negative_height_branch.md)
and the present result put both critical phases of the cap
times conditional product on the full proposed incoming
rectangle. The endpoint source theorem still has its own
specified private-coordinate domain. Equations (15), (21)
do not assert that \(e(a)\) belongs to that domain.

A whole cap estimate must supply the complete endpoint
coefficient on its chosen private contour, the physical
private tails, the two finite Fourier remainders and every
joining current. Nondegeneracy and correct primitive lifts
do not establish these estimates or the nonzero contribution
of the outer saddle. The displaced-contour comparison and
the finite-exception theorem therefore remain open.
