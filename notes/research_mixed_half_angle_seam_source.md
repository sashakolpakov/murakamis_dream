# Retaining the source and geometric deficits at a zero seam

Research deduction, 5 November 2026. The bounds concern the complete
original finite row sums, both parities and every allowed selection.
They refine the source at neighboring angle \(1/2\) and retain the
actual tangent planes. No new geometric cover or sign for the
remaining boundary-potential comparison is asserted.

## 1. The unrounded deficit

Use the phases and finite normalizations of the
[grouped seam reduction](research_mixed_hybrid_zero_pair_reduction.md).
For actual consecutive critical legs \((a,b,c)\), with type indicators
\((\alpha,\beta,\gamma)\), write
\[
 F=\phi_{\alpha\beta}(a,b)+\phi_{\beta\gamma}(b,c),\qquad
 C=F-F_a a-F_c c,\qquad
 \Gamma_{\rm pair}(z_L,z_R)=C+F_a z_L+F_c z_R .
 \tag{1}
\]
The original equation \(F_b=0\) makes (1) the sum of the two
literal tangent planes, independently of the middle real target.
The reference legs may coincide in a short cyclic word; all
incidences remain literal.

Fix \(0<\rho\le1/1000\), a middle target \(x\in[0,\rho]\), and
a total fixed Fourier tolerance \(\delta>0\). Put
\[
 \nu_\rho=-J(\rho),\qquad
 \Delta_\rho=\rho\log2-J(\rho),\qquad
 {\cal D}_s=
 \Re\Gamma_{\rm pair}(z_L,z_R)-A_{\beta,\alpha}-B_\gamma
                  -2\Delta_\rho-\beta\nu_\rho-\delta .
 \tag{2}
\]
Here \(J\) is the continuous periodic real function
\[
 J(y)=\Re\frac{\operatorname{Li}_2(e^{-2\pi i y})-\pi^2/6}{2\pi i},
 \quad J(0)=J(1/2)=J(1)=0,
 \quad J'(y)=\log(2|\sin\pi y|)
 \tag{3}
\]
away from its integer derivative singularities. The source constants
are
\[
 (A_{00},A_{01},A_{10},A_{11})
       =(.360050,.447948,.485081,.551147),\qquad
 (B_0,B_1)=(.347548,.515591).
 \tag{4}
\]
The original allocated raw pair, denoted \({\cal B}_L{\cal B}_R\),
therefore satisfies
\[
 {\cal B}_L{\cal B}_R
 \le C_0N^A\exp N\{\Re\Gamma_{\rm pair}-{\cal D}_s\}.
 \tag{5}
\]
Each kernel in (5) may be replaced by its absolute original row sum.
The other real angles range over the whole period; their heights
belong to separate physical states: type three in \([-.03,.02]\),
unselected type four in \([-.057,0]\), selected type four in
\([0,.014]\). The complex first-argument chirp and selected
Fourier factors are included in (4). The two middle halfweights
recombine into power \(\beta\).

The [completed seam comparison](research_mixed_seam_boundary_potential_reduction.md)
gives \({\cal D}_s>7/25+Q_s\) if \(\delta<3/1000\), where
\(Q_s=(151/20)(\Im a)^2+(11/2)(\Im c)^2\).
This is a lower bound for the actual deficit (2), not its definition.
Retaining (2) can preserve a larger geometric reserve.
In particular \(Q_s\) must not be subtracted a second time from
a comparison already using \({\cal D}_s\). Its interpretation as
the cost of actual exterior blocks still requires the original
isolated-plateau hypotheses.

## 2. The complete source at neighboring angle \(1/2\)

Let
\[
 r_N=e^{-2\pi i/N},\quad
 p_j(X)=\prod_{k=1}^j(1-r_N^kX),\quad P_j=p_j(1),\qquad
 C_{e,N}(X,Y)=\sum_{j=0}^{N-1}
             \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+e}} .
 \tag{6}
\]
At a seam argument \(1\) and another argument \(-1\), either
orientation has absolute row
\[
              \frac{|p_j(-1)|}{|P_j|^{1+e}} .
 \tag{7}
\]
The factor \((-1)^{-j}\), when present, has modulus one.
Also \(d_N(1)=1\) exactly, while the true Fourier bound at
\(-1\) has upper exponential rate zero. This uses the absolute
bound including its forcing term, not a relative inverse-factorial
approximation. Every selected frequency factor at these real
arguments has modulus one.

The [whole-period product estimate](research_mixed_right_half_source_reduction.md)
and its sine-factorial denominator estimate give the row exponent
\[
 f_e(u)=J(u+1/2)-(1+e)J(u),\qquad 0\le u\le1,\quad u=j/N ,
 \tag{8}
\]
with a fixed polynomial prefactor. This includes every row and every
product zero. If \(N\) is even, \(p_j(-1)=0\) for \(j\ge N/2\);
if \(N\) is odd those rows need not vanish and remain in (8).

On \(0<u<1/2\), \(J(u)<0<J(u+1/2)\), and
\[
 \begin{split}
 f_e'(u)&=\log(2\cos\pi u)-(1+e)\log(2\sin\pi u),\\
 f_e''(u)&=-\pi\tan(\pi u)-(1+e)\pi\cot(\pi u)<0 .
 \end{split}
 \tag{9}
\]
The derivative goes from \(+\infty\) to \(-\infty\), so this
interval has one maximum. Periodicity and \(J(1-u)=-J(u)\)
give \(f_e(1-u)=-f_e(u)\); the upper half has nonpositive rate.
Thus the whole-row maximum is exactly
\[
 \begin{split}
 c_0&=-2J(1/4),\qquad u_0=1/4,\\
 c_1&=J(1/2+u_1)-2J(u_1),\qquad
 u_1=\frac1\pi\arcsin\sqrt{\frac{\sqrt{17}-1}{8}} .
 \end{split}
 \tag{10}
\]
Indeed the type-four equation is \(2\cos(\pi u)=4\sin^2(\pi u)\);
for \(v=\sin^2(\pi u)\) it becomes \(4v^2+v-1=0\).
Both maximizers are on the original real interval.
Outward evaluation gives
\[
 .291560<c_0<.291561,\qquad .443533<c_1<.443534 .
 \tag{11}
\]

**Theorem 1.** If both neighboring targets are exactly real \(1/2\),
the complete allocated pair at any \(x\in[0,\rho]\) has upper rate
\[
             c_\beta+c_\gamma+2\Delta_\rho+\beta\nu_\rho+\delta .
 \tag{12}
\]
The estimate holds for all levels, both parities and all allowed
selections, with a fixed polynomial prefactor, and also for both
absolute row sums. No conditional saddle near zero is used.

The same argument works one factor at a time. If just the left
neighbor is real \(1/2\), or just the right neighbor is, respectively,
the pair upper rates are
\[
 \begin{array}{ll}
 c_\beta+B_\gamma+2\Delta_\rho+\beta\nu_\rho+\delta,
     &z_L=1/2,\\
 A_{\beta,\alpha}+c_\gamma+2\Delta_\rho+\beta\nu_\rho+\delta,
     &z_R=1/2 .
 \end{array}
 \tag{12a}
\]
The other neighbor keeps its whole real period and full physical
typed height band. Thus these one-sided refinements do not require
both neighboring coordinates to be at the half-angle.

For the collar, apply the original estimates
\[
 |p_j(e^{-2\pi ix})|/|P_j|\le C_0N^A e^{N\Delta_\rho},
 \qquad |d_N(e^{-2\pi ix})|\le C_0N^A e^{N\nu_\rho}
\]
to the two middle factors and their combined Fourier power. The
changing first-argument chirp is unit modulus because the low
argument is real; the other chirp is unchanged and also unit
modulus at \(-1\). Sum every row and spend the single total
tolerance \(\delta\). On the actual hybrid contour a coordinate
at \(1/2\) has height zero for every seam attenuation, including
when selected.

When both neighbors are real \(1/2\), replace (2) by
\[
 {\cal D}^{1/2}_s={\cal D}_s+
 S_{\alpha\beta\gamma},\qquad
 S_{\alpha\beta\gamma}
       =A_{\beta,\alpha}+B_\gamma-c_\beta-c_\gamma .
 \tag{13}
\]
All eight type choices have \(S_{\alpha\beta\gamma}>.097534\).
For an alternating type-three seam, \((\alpha,\beta,\gamma)=(1,0,1)\),
the saving exceeds \(.228444\). These are source improvements
at the same actual plane. They do not replace the plane itself
or certify a boundary-potential sign.

## 3. A physical neighborhood of the half-angle point

Number the seam endpoint's argument by \(c\in\{0,1\}\), and let
\(d\) be the moving argument's type indicator. Its full raw rate is
\[
 \begin{split}
 R_{e,d,c}^{\sigma}(u;y,h)
   ={}&I_h(u,y)-(1+e)J(u)-2\pi c h u\\
     &+\frac d2\{\max(\nu(y+ih),2\pi h_+)-2\pi\sigma h\},\\
 I_h(u,y)={}&\int_0^u\log|1-e^{2\pi h-2\pi i(y+t)}|\,dt,
 \qquad \nu=-\Re g .
 \end{split}
 \tag{14}
\]
Here \(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\)
on its original branch near \(z=1/2\). The first-argument chirp
and both true Fourier alternatives remain visible.

The integrand has the explicit real form
\[
 L_h(t)=\pi h+\frac12\log\{4(\sin^2\pi t+\sinh^2\pi h)\}.
\]
On a compact height interval it is bounded above and satisfies
\(L_h(t)\ge L_0(t)-\pi|h|\). Its negative tails are uniformly
integrable: \(|\{t\in[0,1]:L_h(t)<-s\}|\le C e^{-s}\).
Truncation below \(-M\) therefore proves joint continuity of
the integral in (14), uniformly in \(u,y,h\), including zeros.
For the finite products, truncate below \(-\log N\). The excess
integral is \(O(1/N)\); the total variation is \(O(\log N)\),
uniformly in \(h\), since \(L_h\) is monotone on each half-period.
The shifted Riemann-sum error is thus \(O(\log N)\). This proves
the uniform all-row product upper bound with a polynomial prefactor.
The denominator estimate is uniform through both row ends. The
[absolute Fourier theorem](research_mixed_fourier_weight_continuation.md)
is uniform on compact subsets of \(0<\Re z<1\), and its displayed
rate is continuous there. The maximum of (14) over \(u\in[0,1]\)
is consequently continuous at \((1/2,0)\), with value \(c_e\).

For every \(\eta>0\), a fixed neighborhood of the two half-angle
targets gives pair upper rate
\[
       c_\beta+c_\gamma+2\Delta_\rho+\beta\nu_\rho+\eta+\delta .
 \tag{15}
\]
One neighborhood works for the finitely many types, orientations and
allowed selections. Intersect it with each selection's physical
height band; no source continuation through the opposite-sign band
is asserted. The collar and constants are fixed independently of
\(N\). This is a source continuity result, not a quantified
neighborhood or a geometric comparison.

## 4. Using actual deficits without double allocation

For this assembly additionally choose \(\rho\) below the fixed
endpoint-thickening radius in the seam boundary reduction, so that
its finite single-edge gap \(d_s=1/4000\) applies. The preceding
raw pair statements need only \(0<\rho\le1/1000\).
For each seam star let \(\widehat{\cal D}_s\) be the deficit (2),
or the actual plane minus an applicable finite source rate in (12),
(12a), or (15). In the last case subtract \(\eta\) as well as
the collar and \(\delta\). In particular (13) is the exact
two-sided half-angle case.
Let nonnegative weights \(\alpha_s\) satisfy
\[
 c_e=\sum_{\substack{s\text{ an endpoint incidence of }e}}
                           \alpha_s\le1 .
 \tag{16}
\]
A loop has two endpoint incidences. Multiply each raw pair bound to
power \(\alpha_s\), and fill edge power \(1-c_e\) with the
established finite endpoint gap \(d_s\). The exact seam loss is
\[
 {\cal L}_{\rm actual}(\alpha)=
 \sum_s\alpha_s\widehat{\cal D}_s
             +d_s\left(|E(S)|-2\sum_s\alpha_s\right).
 \tag{17}
\]
Every original halfweight and row sum is allocated once. This holds
for loops and parallel edges, without division by a zero kernel.

For the following assembly all nonseam coordinates are required to
lie in \((\rho,1/2]\), as in the seam reduction; the earlier raw
pair estimates by themselves allow whole-period neighboring angles.
Use that reduction's exact virtual states and finite subaction
\(V_\rho\). The complete allocated source then has upper rate
\[
 M-{\cal L}_{\rm actual}(\alpha)
   +\sum_I\{V_\rho(v_I^+)-V_\rho(v_I^-)\}
   -\frac\theta6\sum_I\sum_{v\in{\cal O}_I}\Psi(v)+\tau .
 \tag{18}
\]
Only physical half-period packets spend the chosen total tolerance
\(\tau\); the finite deficits already contain their tolerances.
Singleton half-period runs have no path or output triples. There
is no truncation error per run and no additional \(Q_s\) subtraction.
The remaining sign still requires a comparison with the same
boundary potential.

## Reproduction

The focused checker validates the endpoint identities, exact
maximizers and outward values, all eight savings, collar allocation
and current inherited records. It recomputes no geometric cover
and evaluates no boundary potential.

    python3 experiments/check_mixed_half_angle_seam_source.py --precision 256
