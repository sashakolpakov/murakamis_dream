# Transport of the terminal Newton left strip to its central cut

Research deduction, 5 November 2026. The full original phase increases
with the real transform index on the left exterior strip, uniformly
at all Newton-contour heights. This transports its zero-mode currents
to the completed central mixed faces. Two of the proposed Newton
alias comparisons then suffice for the entire finite strip. No raw
face with a freely varying real Newton coordinate is assumed small,
and no new root, parameter cover or numerical check is used here.

## 1. An original-phase monotonicity bound

Use the exact simultaneous interpolant \(\mathcal I_N\) and
phase \(\mathcal T\) from
[the joint zero-mode theorem](research_mixed_terminal_three_joint_zero_mode.md),
equations (1), (15a)--(15e). Put
\[
 c=3/20,\qquad P=[11/50,9/20],\qquad
 I_u=[1/10,2/5],\qquad \eta=3/25.
\tag{1}
\]
The ordinary color is \(w\), with complete value \(-2\).
Throughout the phase calculation set
\(a=y+iH\), \(u=z+ih\), where \(y\in P\), \(z\in I_u\),
and \(|H|,|h|\le\eta\). The transform index \(t\) is real.

**Lemma 1.** For every \(0<t\le c\),
\[
              \Re\mathcal T_t(a;t,u)>\lambda,
              \qquad \lambda=\log(171/170)>0.
\tag{2}
\]
Consequently
\[
 \Re\mathcal T(a;t,u)
 \le\Re\mathcal T(a;c,u)-\lambda(c-t).
\tag{3}
\]

*Proof.* On the original primitive branches,
\[
 \mathcal T_t=g'(a+t)+g'(t+u)-3g'(t)+2\pi ia,
 \qquad g'(v)=\Log(2\sin\pi v)+i\pi(1/2-v).
\tag{4}
\]
Since \(t\) is real, the exact real derivative is
\[
 \Re\mathcal T_t=
 \log\frac{|R-e^{-2\pi i(y+t)}|
                |1-r e^{-2\pi i(z+t)}|}
               {(2\sin\pi t)^3},
 \qquad R=e^{-2\pi H}>0,\quad r=e^{2\pi h}>0.
\tag{5}
\]
In particular the chirp and both height contributions are retained.
The first numerator factor is the product of
\(|1-e^{-2\pi i(a+t)}|\) with \(e^{-2\pi H}\), not a
zero-height substitution.

For \(y+t\in[.22,.60]\),
\(\cos(2\pi(y+t))\le\sin(.06\pi)<1/5\). Hence
\[
 |R-e^{-2\pi i(y+t)}|^2
 >(R-1/5)^2+24/25>(9/10)^2.
\tag{6}
\]
For any angle \(\theta\), minimization over a positive radius
gives
\[
 |1-r e^{-i\theta}|\ge
 \begin{cases}|\sin\theta|,&\cos\theta\ge0,\\
               1,&\cos\theta\le0.
 \end{cases}
\tag{7}
\]
If \(t\le1/10\), then \(z+t\in[.10,.50]\), so (7)
is at least \(\sin(\pi/5)>1/2\). Also
\((2\sin\pi t)^3<(2/3)^3=8/27\). The ratio in (5)
is therefore greater than \(243/160>171/170\).

If \(1/10\le t\le3/20\), then
\(z+t\in[.20,.55]\), and (7) is at least
\(\sin(2\pi/5)=\cos(\pi/10)>19/20\).
Indeed \(\cos x\ge1-x^2/2\) and \(\pi<22/7\) give
\(1-(11/35)^2/2>19/20\). The denominator satisfies
\[
 (2\sin(3\pi/20))^3<(3\pi/10)^3
                    <(33/35)^3<17/20.
\tag{8}
\]
The numerator exceeds \((9/10)(19/20)=171/200\), so the
ratio exceeds \(171/170\). This proves (2), and integration
proves (3). The estimates are independent of the two positive radii;
in particular they include both alias heights and every intervening
vertical join height. \(\square\)

An external allocation \(-\nu g(a)/2\), \(\nu=0,1\), is
independent of \(t\), and therefore does not change this transport.
Neither does an alias penalty depending only on the height of \(u\).

## 2. The exact physical strip and its zero mode

Fix an actual type-three terminal reference \(a_*=A+iH\), with
its original selected height \(h_u=\Im u_*\), action
\(\mathcal P_0\), and allocated plane
\[
 B_\nu(a_*;y)=\Re(\mathcal P_0-\nu g/2)(a_*)
 +\Re(\mathcal P_0'-\nu g'/2)(a_*)(y-A)
 -\frac{(y-A)^2}{2500000}.
\tag{9}
\]
Take \(a=y+iH\), independently for \(y\in P\).
The actual external type-four height is negative whenever
\(\nu=1\); this is the original Fourier-halfweight regime.
The bare phase inequalities also hold on the auxiliary reference
disks, but no different physical Fourier branch is inferred there.

Let \(0<\delta<c\) be a fixed end-index cutoff. Let \(c_{t,N}\)
be the inward lower half-grid cut of the central transform interval,
and let \(J_{u,N}\) be its inward Newton half-grid interval.
Thus \(c\le c_{t,N}\le c+1/N\), and
\(J_{u,N}\subset I_u\). Define the original finite strip by
\[
 S_N^{\rm left}(a,w)=
 \sum_{\delta\le i/N<c_{t,N}}
 \ \sum_{l/N\in J_{u,N}}
              \mathcal I_N(a;i/N,l/N,w).
\tag{10}
\]
The half-grid endpoints are never lattice points. For sufficiently
large \(N\), every included pair satisfies \(i+l<N\).
Thus (10) is a literal sub-sum of the original finite triangle,
including the factor \(N\) already present in \(\mathcal I_N\).

At each retained real \(t=i/N\), apply the exact one-variable
residue splitting in the Newton coordinate, as in
[the alias reduction, equations (5)--(7)](research_mixed_terminal_three_alias_reduction.md):
\[
 S_N^{\rm left}
 =N\sum_{\delta\le i/N<c_{t,N}}
        (I_u+E_u)\mathcal I_N(a;i/N,\cdot,w).
\tag{11}
\]
Here \(I_u\) is the real integral over \(J_{u,N}\), and
\(E_u\) consists of the two alias horizontal sides and four
sign-separated vertical sides of height \(\pm\eta\).
The coefficient in (11) is \(N\), not \(N^2\): the
transform coordinate remains its original physical sum. No
transform-index residue kernel or alias has been introduced.

**Proposition 2 (unconditional zero-mode strip bound).** The
\(I_u\) part of (11), with its original external allocation,
has upper rate at most
\(B_\nu(a_*;y)-1/4000\), uniformly for \(y\in P\),
on a sufficiently small fixed ordinary-color disk and for all
sufficiently large \(N\). The same holds for each fixed ordinary
color derivative after shrinking that disk.

*Proof.* Deform \(I_u\) coherently to its horizontal segment at
height \(h_u\), plus its two oriented vertical joins. On the
horizontal segment, apply (3) pointwise to transport the phase to
\(t=c\). Its anchor values belong exactly to the completed
flattened-transform family \((c,z+ih_u)\). They are below the
original plane by more than \(1/2000\), by
[the completed mixed-face comparison](research_mixed_terminal_three_zero_mode_completion.md#1-the-source-reference-and-completed-face-comparison).

For a vertical join at a Newton cut, first transport its entire
phase pointwise to \(t=c\). Only at that anchor use convexity
in the Newton height. Its endpoints are the completed real-real
corner \((c,c_u)\) and the completed mixed endpoint
\((c,c_u+ih_u)\), both with the same strict reserve. Thus the
new left strip requires no Hessian estimate at \(t<c\).
It also never requires a small raw face \((c,z)\) with free
real \(z\): that real integral is deformed before it is bounded.

For \(t\ge\delta\), every primitive of the simultaneous
interpolation stays in a fixed regular compact strip throughout
these contours and the alias rectangle. For instance
\(\Re(t+a)\ge\delta+.22\) and
\(\Re(t+u)\ge\delta+.10\); both upper endpoints stay
strictly below one. The general factorial/Newton symbol cited in
the joint theorem therefore applies on this compact product even
though it extends to the left of the Hessian rectangle.

The possible physical rows with \(c<t<c_{t,N}\) lie within
\(1/N\) of the anchor. Uniform first derivative bounds on the
regular compact product, rather than an unproved monotonicity
outside (2), pay an \(O(N^{-1})\) rate error for these rows.
The inward Newton cuts have the same controlled perturbation.
Choose a fixed small color disk, then large \(N\), so all such
changes and polynomial factors use less than \(1/4000\) of the
strict reserve. The outer sum contains at most \(N\) original
rows and changes only a polynomial prefactor. This proves the
finite gap. Cauchy's formula on a smaller color disk proves the
fixed-derivative statement. \(\square\)

## 3. Only two Newton alias comparisons remain for this strip

The following two anchor comparisons are sufficient:
\[
 \Re\mathcal T(y+iH;c,z\pm i\eta)-2\pi\eta
 \le B_0(a_*;y)-\delta_A
 \qquad(y\in P,\ z\in I_u),
\tag{12}
\]
for some fixed \(\delta_A>0\). They are restrictions of the
zero-other-height Newton single-alias families \((0,\pm\eta)\)
in the twelve-family alias criterion. No geometric-height transform
alias and no double alias is required for (10).

**Corollary 3 (complete finite left strip, conditional only on
(12)).** Put \(\delta_0=\min(1/2000,\delta_A)\).
For every \(0<\delta'<\delta_0\), the entire allocated
finite strip (10) satisfies
\[
 |\text{allocated }S_N^{\rm left}(y+iH,w)|
       \le \exp\{N(B_\nu(a_*;y)-\delta')\}
\tag{13}
\]
on a fixed sufficiently small ordinary-color disk and for sufficiently
large \(N\). Both parities and all fixed ordinary-color derivatives
are retained. In particular \(\delta_A=1/2000\) permits the
common finite loss \(1/4000\).

*Proof.* On a horizontal alias side the exact residue kernel costs
\(2\pi\eta\). Apply (3) with \(h=\pm\eta\), keeping
that penalty unchanged, and use (12) at the anchor.
On either sign half of a vertical alias side, the exact kernel
costs \(2\pi|h|\). Transport first to \(t=c\), again without
changing the penalty. At this anchor the weighted phase is convex
in \(h\) on each sign half. Its endpoints are one of (12) and
a completed real-real corner with penalty zero. Hence the common
reserve is \(\delta_0\).

The exact half-grid formula bounds the kernel even at height zero,
where its absolute value is \(1/2\). Thus no unestimated small
height interval is removed. All six alias pieces, the three deformed
zero-mode pieces and the outer physical sum are now covered.
The same fixed-color, half-grid and polynomial tolerance argument
as in Proposition 2 proves (13). The external halfweight only adds
its favorable convex Bregman remainder and is counted once.
\(\square\)

## 4. Placement in the original triangular decomposition

Choose \(\delta\) within the already admitted end-index cutoff
of [the terminal transform tail theorem](research_mixed_terminal_transform_tails.md).
That theorem removes the entire original \(i/N<\delta\)
sector with its full Newton sum before any subdivision by \(l\).
We do not infer a bound for arbitrary partial Newton sums inside
that sector from a bound for the coherent full sum.

For the remaining transform indices, (10) is disjoint from the
central rectangle and from the low/high-Newton sectors already
treated. Its complete suppression still requires (12); Proposition 2
already settles its unaliased Newton part. Together these statements
remove a full exterior strip once the two alias comparisons pass,
without a new source cover or a new transform contour. They do not
settle the right transform strip, the remaining lower/upper Newton
bands, or the full ordinary boundary coefficient.
