# The complete first-cap real-row envelope on the early height taper

Research deduction, 7 November 2026. An exact strengthening of the
endpoint curvature pays both lower physical tails. Keeping the actual
upper-height taper also pays the type-three upper tail. Consequently
the complete literal cap, for either own type, has a real-private
profile envelope on the early outgoing strip. This extends an actual
finite-source estimate, not just the regular current domains. The
calibrated cap-plus-ordinary comparison is still a separate problem.
No numerical evaluation or saved-certificate replay is used.

## 1. Original source and the tapered outgoing domain

Use exactly the source, endpoint coefficient and scalar conventions of
[the real-row cap theorem](research_mixed_outer_cap_real_tails.md):
\[
\begin{split}
 U_{\alpha,N}(w,X)
 &=\sum_{i=0}^{N-1}B_{i,N}^{\alpha}(w,z),\qquad
                       X=e^{-2\pi iz},\quad \alpha=0,1,\\
 B_{i,N}^{\alpha}(w,z)
 &=\Delta_N(i/N)^{-1}C_N(i/N,w)
                         \frac{p_i(X)}{P_i^\alpha},\\
 \Delta_N(s)&=\exp\{\pi i[N(s-s^2)-s]/2\}.
\end{split}                                                   \tag{1}
\]
Here \(P_i=(r;r)_i\), \(p_i(X)=(rX;r)_i\),
\(r=e^{-2\pi i/N}\), and \(C_N\) is the whole original
coherent endpoint coefficient. In particular \(|\Delta_N(s)|=1\)
on physical real rows; it is not omitted at complex indices.

Let
\[
\begin{split}
 z&=x+ih,\qquad \frac1{10}\le x\le\frac{11}{50},\\
 -\frac{27}{250}&\le h\le\frac7{40}(x-1/10).
\end{split}                                                   \tag{2}
\]
Every unselected early first-coordinate taper lies in (2): its
positive original height is at most \(.021\), and its cutoff is
at most \((x-.1)/.12\). Additional neighboring cutoffs only
reduce this positive height. Negative original attached heights
are at least \(-.108\). No independent positive height \(.021\)
is permitted at the left endpoint \(x=.1\).

Write \(\lambda(s)=\Re S(s)\), with the actual full-index
endpoint action from
[the original coefficient theorem](research_complete_boundary_full_index_interval.md).
The physical-row upper rate is
\[
\begin{split}
 R_\alpha(s,z)&=\lambda(s)+I_h(s,x)-\alpha J(s),\\
 I_h(s,x)&=\int_0^s\log|1-e^{2\pi h-2\pi i(x+t)}|\,dt.
\end{split}                                                   \tag{3}
\]
This is the rate of (1), including all rows revived off the outgoing
physical grid. The integrated logarithm is continuous through its
zeros. On every fixed compact subinterval of \(0<s<1\), the
original coefficient packet and zero-safe factorial bounds give
the finite row estimate with rate (3), an arbitrarily small
additive tolerance, and a polynomial prefactor.

## 2. A stronger exact endpoint curvature on the real half interval

**Lemma 1.** On \(0<s<1/2\),
\[
 -\frac{\lambda''(s)}\pi
 =\cot\pi s+
    \frac{2}{\sin\pi s}
       \Re\frac1{\sqrt{2-e^{-2\pi is}}}
 >\cot\pi s.                                             \tag{4}
\]
The square root in (4) is the principal one with positive real part.

*Proof.* The original endpoint critical point gives
\(U=e^{2\pi iu_c(s)}\) and \(E=e^{-2\pi is}\).
Proposition 2 of the
[exact curvature formulas](research_mixed_pair_curvature_composition.md)
proves, on that original branch,
\[
\begin{split}
 \mathfrak r&=\frac{(U+1)(3U-1)}{5U^2-2U+1},\qquad
          \mathfrak r^2=E(2-E),\\
 -S''(s)/\pi&=\cot\pi s+\frac{2(\cot\pi s-i)}{\mathfrak r}.
\end{split}                                                   \tag{5}
\]
No sign of a square root may be chosen independently here.
The original explicit endpoint branch has \(u_c(s)\to0\)
as \(s\downarrow0\): in its formula
\(\sqrt{1-2e^{2\pi is}}\to-i\), so the argument of the
specified arctangent tends to zero. Thus \(U\to1\) and
\(\mathfrak r\to1\). Throughout this connected real interval,
\(E(2-E)\ne0\). The continuous square root with this limit is
therefore exactly
\[
              \mathfrak r=e^{-\pi is}\sqrt{2-e^{-2\pi is}}.
                                                               \tag{6}
\]
Indeed \(\Re(2-e^{-2\pi is})>1\), so its indicated square
root is single-valued and has positive real part. Substituting
\(\cot\pi s-i=e^{-\pi is}/\sin\pi s\) into (5) proves
(4). The reciprocal of a nonzero number with positive real part
also has positive real part, giving the strict inequality.
\(\square\)

This is stronger than the previously used \(\lambda''<0\),
and involves the actual coherent endpoint action, not the entropy
of its separate Newton rows.

**Corollary 2.** For either \(\alpha\), every outgoing target
with \(.1\le x\le.22\), and every finite height \(h\),
\[
 R_\alpha''(s,z)<0\quad(0<s<1/2),\qquad
 R_\alpha'(s,z)>13/100\quad(0<s\le.27).                  \tag{7}
\]

*Proof.* Away from a zero,
\[
 R_\alpha''=\lambda''+
     \pi\Re\cot\pi(s+x+ih)-\alpha\pi\cot\pi s.
                                                               \tag{8}
\]
If \(s+x<1/2\), then
\(\Re\cot\pi(s+x+ih)\le\cot\pi(s+x)<\cot\pi s\).
If \(s+x\ge1/2\), its real part is nonpositive, since
\(s+x<.72<1\). Equation (4) proves strict concavity in both
cases, including \(\alpha=0\).

At \(s=.27\), one has \(.37\le s+x\le.49\); the cosine
of twice this angle is negative. Hence
\(|1-e^{2\pi h-2\pi i(s+x)}|>1\) at every height.
The inherited original scalar bounds
\(\lambda'(.27)>27/50\) and \(J'(.27)<41/100\),
recorded in (12a) of the real-row theorem, imply
\(R_\alpha'(.27,z)>13/100\). Strict concavity gives (7)
at every smaller positive index. The conclusion is continuous
at any integrated-logarithm zero. \(\square\)

In particular the compact lower tail reduces to its original cut
\(.27\). The old argument requiring outgoing real coordinate
at least \(.22\) is not used.

## 3. Both upper physical tails on the actual taper

The exact original upper-index identity gives
\[
 \lambda'(s)-J'(s)\le-\log4\quad(1/2\le s<1),
                    \qquad \lambda'(1/2)=-\log2.         \tag{9}
\]
For the short bridge, (4) also supplies the elementary estimate
\[
                    -\lambda''(s)<\frac{19}{5}
                          \quad(.49\le s\le.5).         \tag{10}
\]
To check it, use
\(\cot\pi s<1/30\), \(\sin\pi s>99/100\), and
\(2-\cos2\pi s>299/100>(19/11)^2\).
Thus the right side of (4) is less than
\(1/30+2200/1881\), and
\[
        \frac{22}{7}\left(\frac1{30}+\frac{2200}{1881}\right)
                                    <\frac{19}{5}.
\]
These trigonometric bounds follow from
\(\tan(.01\pi)<1/30\) and
\(\cos(.02\pi)>99/100\), using the elementary sine/cosine
polynomials and \(\pi<22/7\). Combining (9)--(10) yields
\[
            \lambda'(.49)<-\log2+\frac{19}{500}.         \tag{11}
\]

**Lemma 3.** On (2), both \(R_0(s,z)\) and \(R_1(s,z)\)
are strictly decreasing for \(.49\le s<1\).

*Proof for type three.* Write \(x=.1+d\),
\(0\le d\le.12\), and \(k=7/40\).
For \(.49\le s\le.5\), set \(a=s+x-.5\).
Then \(.09\le a\le.22\), and the numerator modulus is
\[
 |1-e^{2\pi h-2\pi i(s+x)}|^2
          =1+v^2+2v\cos(2\pi a),\qquad v=e^{2\pi h}.
                                                               \tag{12}
\]
The cosine is positive. If \(h\le0\), this increases with
\(v\le1\), so it is at most its value at \(h=0\).
If \(0<h\le kd\), it is at most its value at \(h=kd\).
For either bound it decreases as \(s\) increases. At \(s=.49\),
differentiate its value at \(h=kd\) with respect to \(d\).
After division by \(4\pi e^{2\pi kd}\), the derivative is
\[
 k\{e^{2\pi kd}+\cos(2\pi(.09+d))\}
                    -\sin(2\pi(.09+d))<0.               \tag{13}
\]
Indeed \(e^{2\pi kd}<6/5\), the cosine is at most one,
and the sine exceeds \(1/2\). Therefore its upper bound is
\((7/40)(6/5+1)-1/2<0\). For the exponential bound use
\(2\pi kd\le.042\pi<33/250\) and
\(e^u\le(1-u)^{-1}<6/5\); for the sine use
\(.18\pi\le2\pi(.09+d)\le.42\pi\).
Consequently (12) is always at most \(4\cos^2(.09\pi)\).
Equations (11)--(12) give throughout the bridge
\[
 R_0'(s,z)<\frac{19}{500}+\log\cos(.09\pi)
 \le\frac{19}{500}-\frac{81\pi^2}{20000}
 <-\frac1{1000}.                                        \tag{14}
\]
Here \(\log\cos u\le-u^2/2\), and \(\pi>157/50\)
proves the last strict rational comparison.

For \(s\ge.5\), the original identity (9) and
\(\sin\pi s\,|\sin\pi(s+x)|\le\cos\pi x\) give
\[
 e^{R_0'(s,z)}
       \le e^{\pi h}
               \sqrt{\cos^2\pi x+\sinh^2\pi h}.
                                                               \tag{15}
\]
The square of the right side is
\(\{1+v^2+2v\cos(2\pi x)\}/4\).
Exactly the comparison (12)--(13), now with
\(x=.1+d\), bounds it by \(\cos^2(.1\pi)<1\).
The sine in (13) is then between \(\sin(.2\pi)\) and
\(\sin(.44\pi)\), and still exceeds \(1/2\).
This proves the upper-tail direction for type three, with the
positive taper retained rather than replaced by an independent
height interval.

*Type four.* On (2),
\(|1-e^{2\pi h-2\pi i(s+x)}|\le1+e^{.042\pi}<9/4\).
On the bridge the inherited bounds
\(\lambda'<-3/5\), \(J'>3/5\), and
\(\log(9/4)<6/5\) prove \(R_1'<0\).
For \(s\ge.5\), (9) gives
\(R_1'<\log(9/16)<0\).
All monotonic statements extend through zeros by integration on
the adjoining intervals and continuity of (3). \(\square\)

## 4. The true index ends and the complete finite envelope

The small-index Newton estimate in Section 3 of the real-row
theorem uses only \(h\le.021\), not a lower bound on \(x\).
It therefore retains the rate ceiling \(1/4\) for \(s\le.01\).
For \(s=1-\delta\), \(0\le\delta\le.01\), its exact
coefficient estimate retains the ceiling
\(3/5+\delta\log2\). In the full-product identity
\[
 p_i(X)=\frac{1-X^N}{\prod_{j=i+1}^{N}(1-r^jX)},          \tag{16}
\]
the denominator angles modulo one now lie in \([.09,.22]\).
Every factor has modulus greater than \(1/2\), uniformly in
its radius: minimize over that radius and use
\(\sin(.18\pi)>1/2\). Thus
\[
 |p_i(X)|\le2e^{2\pi Nh_+}2^{N-i}.                      \tag{17}
\]
The remaining reciprocal own factorial has nonpositive rate for
\(s\ge.99\). The resulting upper endpoint ceiling is
\[
 E_{\rm end}(h):=\frac35+2\pi h_++\frac1{100}\log4
          <\frac{373}{500}<\frac34.                    \tag{18}
\]
Use \(h_+\le.021\), \(\pi<22/7\), and
\(\log4<7/5\); the latter follows from the positive
exponential polynomial through degree five at \(7/5\).
For \(h\le0\), (18) is less than \(123/200<5/8\).
All these estimates are zero-safe finite-product bounds.

Define, without a new critical point,
\[
 A^{\rm real}_\alpha(z)=
       \max_{.27\le s\le.49} R_\alpha(s,z)
       =\max_{.27\le s\le.49}\Re\Psi_\alpha(s,z).
                                                               \tag{19}
\]
The equality uses the original bare cap phase; its scalar correction
\(-i\pi(s-s^2)/2\) has zero real part on real \(s\).

**Theorem 4.** Uniformly on (2), both own types have the complete
finite-source bound
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi iz})|
 \le C_\eta N^{a_\eta}
 \left[
 e^{N\{A^{\rm real}_\alpha(z)-c(1-\cos\theta)+\eta\}}
       +e^{N\{E_{\rm end}(h)+\eta\}}
 \right],\qquad -\pi\le\theta\le\pi,                   \tag{20}
\]
for some \(c>0\) and every \(\eta>0\). Both level parities
and each fixed ordinary-color derivative have the same exponents
with suitable polynomial factors.

*Proof.* Keep the coherent coefficient before applying a triangle
inequality to the physical private-index sum (1). On
\([.01,.99]\), the
[full real-color endpoint estimate](research_mixed_endpoint_real_color_decay.md)
supplies a common positive angular loss in its original coefficient
rate \(\lambda(s)\). The remaining factors are color independent.
Corollary 2 and Lemma 3 reduce the two compact tails to their real
cut values, both of which belong to the maximum (19). Sum these
rows and the central rows with their original zero-safe factorial
errors. The at most \(N\) summands cost only a polynomial.

At the two true ends use the original finite Newton estimates:
\(V_\theta\le V_0\) on lower-half rows and
\(V_\theta\le0\) on upper-half rows. Equations (16)--(18)
then give the second exponent; no angular loss is asserted there.
The same source theorems include fixed derivatives and both
parities. Aggregate the finitely many additive tolerances into
\(\eta\). \(\square\)

The theorem estimates the whole literal cap, including physical
rows that revive at complex outgoing targets. It performs no
off-grid identification and introduces no new private contour.
The private aliases are separately below (19) by more than
\(1/20\), as proved in
[the alias-payment deduction](research_mixed_cap_alias_half_and_private_payment.md),
but (20) already follows directly from the coherent physical sum.

Multiplying (20) by the exact neighboring ordinary factors and
complete Fourier weights is legitimate. Their original marginals,
middle energy and relative pinning fee must still be kept. The
remaining calibrated comparison involves (19) and the explicit
endpoint ceiling (18) on the actual tapered target; neither is
replaced here by the cap plane at its original height. Thus the
finite-source domain obstruction for these physical tails is
removed, while the compensated deep-boundary sign remains open.
