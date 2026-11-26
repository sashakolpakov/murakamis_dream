# The last conditional source on the ordinary endpoint images

Research reduction, 5 November 2026. The original one-cap torus source
can be retained without introducing a new closing Gram polynomial.
Its last conditional factor requires four correlated endpoint-image
families. The old conditional curvature and left real-tail estimates
already apply to these families. The complete packet reduces to the
explicit boundary inequalities below; those new inequalities are not
asserted as certified here. A bounded diagnostic using existing
proposals is recorded separately.

## 1. The actual terminal variables and their smallest available domains

For an open word of length \(m\ge2\), the
[one-cap identity](research_mixed_conditional_torus_composition.md),
Corollary 3, retains the final two factors
\[
 C_{\epsilon_m,N}(X_{m-1},X_m)
       \mathcal H_N(w_R,X_m^{-1}),\qquad
 X_j=e^{-2\pi i t_j}.
 \tag{1}
\]
At its original geometric point put \(a=t_{m-1}\), \(e=t_m\),
and \(t=s_m\). Thus \(e\) is private, \(t\) is the row summed in
the last conditional, and \(a\) is the external attached leg of the
preceding vertex. The kernel's own type is \(3+\epsilon_m\);
the type of \(a\) is the preceding vertex's type.

The [endpoint maps](research_mixed_open_word_critical_localization.md)
give, for each \(\epsilon,\delta\in\{0,1\}\), a holomorphic map
\[
 a\in D_{3+\delta}\longmapsto(e(a),t(a),u(a)),\qquad
 D_3=\{|a-(.35-.01i)|\le.09\},\quad
 D_4=\{|a-(.30-.052i)|\le.064\}.
 \tag{2}
\]
The graph
\[
 \mathcal K_{\epsilon,\delta}
       =\{(a,e(a)):a\in D_{3+\delta}\}
 \tag{3}
\]
is sufficient. There is no need to enlarge it to an independent
product of a disk and a private rectangle. The exact
[endpoint image extraction](research_mixed_open_word_endpoint_rectangles.md)
gives

| Own type | \(e(a)\) | \(t(a)\) |
|---|---|---|
| Three | \((.376,.438)+i(-.019,.037)\) | \((.278,.391)+i(-.072,.021)\) |
| Four | \((.333,.363)+i(-.051,-.019)\) | \((.246,.350)+i(-.108,-.020)\) |

At length two the preceding leg is the other endpoint's attached
leg, still in (2), so these same four families apply. Length one
has no conditional kernel in the one-cap formula and is not an
additional family in (3).

The independent source rectangles previously proved for the full
right square have height bands \([-.03,.02]\) and
\([-.057,.0141]\). They do not contain (2): the disk heights reach
\(-.10,.08\) and \(-.116,.012\), respectively. The private type-three
height can also exceed .02. Neither unspecified neighborhood
continuation nor the refined cyclic height boxes supplies the
missing inclusion.

## 2. The original root and the analytic contour inputs already proved

Use the unchanged finite conditional source
\[
\begin{split}
 \mathcal L_{\epsilon,N}(a,e)
 &=\widehat P_N(Na)\widehat P_N(Ne)
       C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ie}),\\
 Q_\epsilon(s;a,e)
 &=g(s+a)+g(s+e)-(2+\epsilon)g(s)+2\pi ias,\\
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
\end{split}
\tag{4}
\]
The fixed sum contains all \(0\le j<N\) rows, including their
off-grid revival. Both marked factorials and every logarithmic
lift are the original ones.

The attached endpoint equation is exactly
\[
 Q_{\epsilon,s}(t(a);a,e(a))=0.
 \tag{5}
\]
Indeed \(g'(z)=J'(z)+i\pi(1/2-z)\) on the original strip,
and (5) becomes the second equation of the endpoint-map theorem.
Thus no new root proposal or polynomial-to-logarithm identification
is needed for this conditional branch.

Both parameters lie strictly in
\(\mathcal Q=\{.23<\Re z<.45,\ |\Im z|<.12\}\).
The [old conditional contour lemma](research_mixed_conditional_image_contours.md),
Lemma 2, therefore gives
\[
 -\Re Q_{\epsilon,ss}(s;a,e)>1/8
 \quad\text{on}\quad
 K=[.15,.49]+i[-.20,.20].
 \tag{6}
\]
The root in the table is inside \(K\), at real distance greater
than .09 from its two real cuts. Negative real derivative gives
uniqueness on this convex rectangle and identifies the original
Gaussian branch. The implicit function theorem supplies the root
on an ambient neighborhood of the compact graph (3), with the
same uniqueness on overlaps. All central factorial arguments have
real parts in \((0,1)\).

For \(0\le v\le1\), retain the full periodic real-row upper rate
\[
\begin{split}
 H_\epsilon(v;a,e)
 ={}&\Re g(a)+\Re g(e)
 +\int_0^v\log|1-e^{-2\pi i(a+x)}|\,dx\\
 &+\int_0^v\log|1-e^{-2\pi i(e+x)}|\,dx
 -(2+\epsilon)J(v)-2\pi v\Im a .
\end{split}
\tag{7}
\]
At integrable zeros this denotes its continuous value. The same
old lemma proves
\[
 H_\epsilon'(v)\ge\log4-.24\pi>1/2
                    \qquad(0<v\le.15).
 \tag{8}
\]
The entire left tail is therefore controlled by its .15 cut.
These two analytic inputs are genuine domain inclusions; no
cyclic reference refinement is used.

## 3. Four boundary-circle source tests suffice

Put \(\ell=.15\), \(b=.49\), \(h=.20\), and
\(M(a)=\Re Q_\epsilon(t(a);a,e(a))\).
For a complex \(z\) in \(\mathcal Q\), define
\[
 c_z=\cos\pi z,\quad d_z=\sin\pi z,\quad
 q_z=\frac{\sin(2\pi\Re z)}
             {\cosh(2\pi\Im z)-\cos(2\pi\Re z)}.
 \tag{9}
\]
For every point of each of the four boundary circles in (2),
the following inequalities, with a common \(\eta>0\), are sufficient:
\[
\begin{split}
 M-\Re Q_\epsilon(c;a,e)&\ge\eta
                                      &&(c=\ell,b),\\
 M-\Re g(a)-\Re g(e)
  -2\pi(-\Im a)_+-2\pi(\Im e)_+&\ge\eta,\\
 M-\Re Q_\epsilon(x\pm ih;a,e)+2\pi h&\ge\eta
                                      &&(\ell\le x\le b).
\end{split}
\tag{10}
\]
The second line is exactly the revived last-row gap. In a
holomorphic test it is the minimum over \(v,w\in\{0,1\}\) of
\[
 \Re\{Q_\epsilon(t;a,e)-g(a)-g(e)-2\pi iv a+2\pi iw e\}.
 \tag{11}
\]
Both growth factors remain present, even when one parameter changes
the sign of its height.
At either real cut \(c=\ell,b\), both shifted arguments
\(c+a,c+e\) remain in the original strip, and the exact logarithmic
product primitive gives \(H_\epsilon(c;a,e)=\Re Q_\epsilon(c;a,e)\).
Thus the cut comparisons in (10) are precisely the endpoints of
the full real-tail rate (7).

The supplementary right-tail shape test is
\[
\begin{split}
 &4^{-\epsilon}e^{2\pi(\Im e-\Im a)}
 |c_a-\omega d_a|^2|c_e-\omega d_e|^2
                      (1+\omega^2)^\epsilon<1,\\
 &\hspace{24mm}
 -\cot(\pi b)\le\omega\le\max(q_a,q_e).
\end{split}
\tag{12}
\]
This is the exact quartic/sextic of the old contour lemma.
After its two quadratic vertices the factors are increasing;
the real tail first decreases and then increases. Hence its
maximum on \([b,1]\) is at \(b\) or 1. It is not legitimate to
discard the second endpoint.

**Proposition 1.** If (10)--(12) hold on the four complete circles,
then the literal conditional source has its original nonzero
packet on a fixed ambient complex neighborhood of every graph (3):
\[
 \mathcal L_{\epsilon,N}(a,e)
 =N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}A_\epsilon(t;a,e)}
      {\sqrt{-Q_{\epsilon,ss}(t;a,e)}}
 e^{NQ_\epsilon(t;a,e)}(1+O(N^{-1})).
 \tag{13}
\]
Here \(t\) denotes the original root continued from (5), and
\[
 A_\epsilon(t;a,e)
 =e^{\pi i(\epsilon t-a-e)/2}
   \frac{\sqrt{2\sin\pi(t+a)}\sqrt{2\sin\pi(t+e)}}
        {(2\sin\pi t)^{1+\epsilon/2}} .
 \tag{14}
\]
The expansion retains both parities and every fixed holomorphic
derivative on smaller neighborhoods. For the literal kernel \(C\)
one divides by the two original marked factorials; its power is
\(N^{-(1+\epsilon)/2}\) and its phase is
\(Q_\epsilon(t)-g(a)-g(e)\).

*Proof.* The hypotheses and (8), (12) control the whole real
complement on each boundary circle. The zero-uniform original
finite-product estimate converts (7) to a polynomial-times-exponential
bound without dividing by a revived zero. For each fixed row
coordinate \(v\), the function
\(H_\epsilon(v;a,e(a))-M(a)\) is subharmonic in \(a\):
each integral in (7) is an integral of logarithms of holomorphic
moduli, and the remaining terms are harmonic. Thus its strict
boundary upper bound also holds throughout the disk. The cut and
horizontal-alias gaps are harmonic in \(a\), so their inequalities
extend there as well.

This argument transfers the actual real-tail gap, not a presumed
extension of the polynomial shape test (12). Uniform continuity of
the zero-safe integral in (7), together with compactness and the
strict gaps, then gives the same estimates with smaller margins
on an ambient neighborhood of (3). This step is needed: a normalized
packet on a one-complex-dimensional graph alone would not imply
transverse parameter derivatives.

Apply the unchanged cotangent residue contour to the central rows.
Its constant mode is \(+N\); both horizontal aliases have their
penalties \(2\pi h\). Imaginary convexity from (6) controls all
half-grid vertical currents using (10). Move only the zero mode
to the critical height. Its endpoints there have loss greater than
\((.09)^2/16\), and the real cut gaps control the other endpoints
of the two joins. Every original current is thereby retained.
Strict margins survive half-grid rounding. The usual nonzero
factorial symbol, this \(+N\), and its one Gaussian give (13).
The normalized holomorphic remainder and Cauchy's formula give
the stated fixed derivatives and higher orders. \(\square\)

## 4. Exact external derivatives and finite scope

The existing three-variable endpoint Jacobian gives \(e'(a)\);
there is no need to differentiate a floating proposal. For a
fixed contour point \(c\), stationarity gives
\[
\begin{split}
 \frac d{da}\{Q_\epsilon(t;a,e)-Q_\epsilon(c;a,e)\}
 ={}&g'(t+a)-g'(c+a)+2\pi i(t-c)\\
   &+[g'(t+e)-g'(c+e)]\,e'(a).
\end{split}
\tag{15}
\]
For the four last-row branches (11), the derivative is
\[
 g'(t+a)+2\pi it-g'(a)-2\pi iv
   +[g'(t+e)-g'(e)+2\pi iw]\,e'(a).
 \tag{16}
\]
Thus an outward check can reuse the existing root witnesses,
their original logarithmic branch, and the implicit response of
the same endpoint equations. Only these new source inequalities
need evaluation. For the horizontal segments, (6) permits whole
real-interval bounds by concavity tangents. Four circle families
are sufficient; no enumeration of open-word lengths is involved.

The original one-cap torus formula, its scalar
\(\kappa^{m+\sum\epsilon_j}N^{m+\sum\epsilon_j}\), and every
factor \(d_N(X_j)(1+X_j^{-N})\) remain unchanged.
The right ordinary polynomial is still related exactly by
\(\mathcal H_N(w,e^{2\pi ie})=G_N(Ne)\mathcal C_N(e,w)\)
to the proved endpoint coefficient. Proposition 1 would supply
the missing terminal \(C\) germ; it would not discard either
Fourier branch or prove the remaining open-word contour gap.

The [bounded diagnostic archive](../repro/diagnostics/2026-11-05-terminal-conditional-images/README.md)
reuses 132 old endpoint-map proposals, without a root solve or
optimization. Its sampled cut/last-row margins are positive,
as are both sampled horizontal-alias margins; the sampled
right-tail polynomials are below one. Those samples establish
none of (10)--(12) on a complete circle or interval. No new
conditional packet or open-word noncancellation theorem is
promoted by that diagnostic.
