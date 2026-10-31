# Exact root-character contraction and a correlated spectral localization lemma

31 October 2026. Internally reviewed original-source theorem. The exact
root-character contraction retains the full repeated-root algebra and
all first normal directions. A correlated spectral estimate proves the
whole-source alias and physical-color gaps for every fixed root star
$C(hT(h^s))$, $s\ge2$, with independent colors and arbitrary retained
half-twist signs. This is a source theorem, separate from the marked
geometric and whole-period steps needed for a filled-knot conclusion.
No corresponding spectral estimate for an arbitrary turned child is
assumed.

The missing winding in the exact Fourier identity was already proved in
[the outer squared-kernel theorem](actual_outer_color_squared_kernel.md),
§§1–4. The residue calculation and periodic endpoint repair below provide
an alternative proof and retain the same normal-coordinate cancellation.
[The prior-source comparison](actual_conway_root_star_prior_source_coverage.md)
also records the exact all-inner-odd belt-source overlap; no novelty or
topological classification is asserted.

## 1. Source normalization and exact rerooting

Put $d=N-1$, $q=e^{\pi i/N}$, $\kappa=q^{d^2/2}$, and
$P_N(z)=2T_N(z/2)+2$. The physical pair algebra is
$\mathcal H_N=\mathbb C[z]/(P_N)$.
The actual marked closure and normalized Newton basis obey

$$
\begin{aligned}
\phi(f)&=(-1)^dN^2[z^d](f\bmod P_N),\\
\phi(\widehat B_i\widehat B_j)&=\mathbf1_{i+j=d},\\
T\widehat B_i&=\widehat B_{d-i}.
\end{aligned}
$$

These are the original source identities in
[the exact source compiler](actual_conway_single_leaf_source_composition.md),
§1, and [the finite invariant normalization](../manuscript/sections/02-finite-source.tex). In particular
T is a linear involution, not an algebra automorphism. Coefficient reversal
gives, for all $F,G\in\mathcal H_N$,

$$
\phi((TF)G)=\phi(F(TG)),\qquad
\phi((TF)(TG))=\phi(FG).\tag{1}
$$

The actual circle is $L_j=(-1)^{j-1}U_{j-1}(z/2)$, $1\le j\le N$.
A retained half twist is the original $R^\varepsilon$,
$\varepsilon\in\{0,+1,-1\}$.
Consequently the literal root-leaf contraction is

$$
\phi\bigl(T(R^\varepsilon L_j)T(E)\bigr)
 =\phi(R^\varepsilon L_jE).\tag{2}
$$

All child colors, all half twists in E, the root color j, the marked
closure and the normal coefficients remain unchanged. Equation (2) is a
scalar source identity. No tangle isotopy or new framing follows from it.

## 2. A finite Fourier formula retaining every winding and normal

Let F(z) be ANY polynomial representative, not necessarily reduced modulo
$P_N$. Write its finite symmetric Laurent expansion as

$$
F(w+w^{-1})=\sum_{r\in\mathbb Z}a_rw^r,
\qquad a_{-r}=a_r.
$$

Then, for $0\le h\le d$,

$$
\phi(L_{N-h}F)=(-1)^hN^2
 \sum_{m\in\mathbb Z}(-1)^m(m+1)a_{h+mN}.\tag{3}
$$

The sum is finite. In particular its $m=-1$ term is IDENTICALLY ZERO.
If $\deg F\le d$, only $m=0$ can contribute, and the answer is
$(-1)^hN^2a_h$. The general formula allows one to leave a whole child
product unreduced; the other terms are not optional error terms.

Proof. The coefficient-at-infinity form of the closure is
$(-1)^dN^2$ times the coefficient of $z^{-1}$ in $F(z)/P_N(z)$.
For $z=w+w^{-1}$, use

$$
\begin{aligned}
P_N(w+w^{-1})&=w^{-N}(w^N+1)^2,\\
U_{N-h-1}\!\left(\frac{w+w^{-1}}2\right)
 &=\frac{w^{N-h}-w^{-(N-h)}}{w-w^{-1}},\\
dz&=(1-w^{-2})\,dw.
\end{aligned}
$$

After including the sign of $L_{N-h}$, the desired coefficient is
$(-1)^hN^2$ times the coefficient of $w^{-1}$ in

$$
F(w+w^{-1})\frac{w^{2N-h-1}-w^{h-1}}{(w^N+1)^2}.
$$

Expansion at infinity gives

$$
\sum_{m\ge0}(-1)^m(m+1)
 \bigl[a_{h+mN}-a_{2N-h+mN}\bigr].
$$

Use $a_{-r}=a_r$ and set $m=-n$ in the second half to obtain (3).
This residue computation automatically reduces modulo the FULL $P_N$;
there is no semisimple quotient.

There is an equivalent finite Hermite sampling formula. Put

$$
\theta_\ell=\frac{(2\ell+1)\pi}{N},\qquad
w_\ell=e^{i\theta_\ell},\qquad c_\ell=w_\ell+w_\ell^{-1},
\qquad0\le\ell<N.
$$

Then

$$
\phi(L_{N-h}F)=(-1)^h\sum_{\ell=0}^{N-1}w_\ell^{-h}
 \left[(N-h)F(c_\ell)+(w_\ell-w_\ell^{-1})F'(c_\ell)\right].\tag{4}
$$

Indeed discrete Fourier orthogonality yields
$N^{-1}\sum_\ell w_\ell^{-h}A(w_\ell)=\sum_m(-1)^m a_{h+mN}$, while applying
$w\,d/dw$ to A gives the same sum weighted by $h+mN$. Their combination
$(1-h/N)A+N^{-1}wA'$ gives precisely $m+1$. Formula (4) counts each double
node twice and the odd simple node once. At the latter $\theta=\pi$, the
factor multiplying F' vanishes. At $h=0$ it gives the familiar exact
$\phi(L_NF)=N\sum_\ell F(c_\ell)$: the derivative terms cancel in conjugate pairs.

## 3. Replace the root crossing by its exact analytic Hermite chirp

Choose the literal branch

$$
\rho_{\varepsilon,N}(\theta)=\kappa^\varepsilon
 \exp\!\left[i\varepsilon\left(\frac\pi2-\frac\pi{4N}
                  -\frac{N\pi}4\right)\right]
 \exp\!\left[\frac{i\varepsilon N(\theta-\pi)^2}{4\pi}\right].\tag{5}
$$

At every $\theta_\ell$, this equals the original $R^\varepsilon(c_\ell)$, since
$R(c_k)=\kappa(-1)^kq^{k(k+1)}$. On $0<\theta<\pi$ its logarithmic
angular derivative is $i\varepsilon N(\theta-\pi)/(2\pi)$. The original normal
formula

$$
\frac{R'(c_k)}{R(c_k)}
 =-\frac{d-2k}{2(q^{2k+1}-q^{-2k-1})}.
$$

multiplied by $dc/d\theta=-2\sin\theta$ gives exactly that derivative.
Reflection $\theta\mapsto2\pi-\theta$ gives the second occurrence of every double
node. The odd simple node has no normal obligation. Thus, for

$$
\mathcal E_N(\theta)=E_N(2\cos\theta),\qquad
F_N(\theta)=\rho_{\varepsilon,N}(\theta)\mathcal E_N(\theta).
$$

(2) is EXACTLY

$$
Z_{N,h}=(-1)^h\sum_{\ell=0}^{N-1}e^{-ih\theta_\ell}
 \left[(N-h)F_N(\theta_\ell)-iF_N'(\theta_\ell)\right].\tag{6}
$$

No off-grid polynomial estimate for R has been used. In particular the
linear exponential cost of bounding its canonical polynomial off the
real interval is absent.

## 4. A whole-child spectral hypothesis and its consequences

Here is a concrete analytic sufficient condition on the ENTIRE child,
not a bound imposed separately on the root alias. Suppose fixed
$F_*,c,C,\eta_0>0$ and $A_N>0$ satisfy $\log A_N=o(N)$, uniformly over any allowed
child-color family, and

$$
|\mathcal E_N(\theta+iy)|
 \le A_N\exp\!\left(N\left[F_*-c(\theta-\pi)^2+Cy^2\right]\right),
\qquad0\le\theta\le2\pi,\quad |y|\le\eta_0.\tag{7}
$$

Here $A_N$ is a scalar subexponential prefactor. The hypothesis is invariant under any scalar
phase in the child. All constants are independent of its physical colors.

Then the original root contraction obeys

$$
\max_{0\le h\le d}|Z_{N,h}|
 \le\exp\!\left(N[F_*+o(1)]\right).\tag{8}
$$

and for every fixed $\delta>0$ there is $\gamma_\delta>0$ such that

$$
\delta N\le h\le d
 \quad\Longrightarrow\quad
 |Z_{N,h}|\le e^{N(F_*-\gamma_\delta)}.\tag{9}
$$

for all sufficiently large N, at BOTH parities and every root half sign.
The o(1) and threshold are uniform over the stated child family.
A uniform loss in $F_*$ in (7) propagates to (8).

The elementary upper (8) follows directly from (6), using Cauchy's
estimate on a radius 1/N disk for $\mathcal E_N$ and the explicit chirp derivative.
The resulting cost is polynomial in N; periodicity of $\mathcal E_N$ handles the
endpoint disks. The 1/N shifts cost only a bounded exponential factor.

The proof of (9), including the joining currents, occupies Section 5.
Its essential feature is the exact missing $m=-1$ term. If the circle color
$j=N-h$ is small, the nearest folded Fourier mode would otherwise be -j.
That mode has zero weight. Therefore (9) applies to ALL $j\le(1-\delta)N$,
not merely to a folded half-color range.

## 5. Proof of the far-color estimate, with both endpoint currents

Write $u=\theta-\pi$. The chirp has modulus $e^{-\varepsilon Nuy/(2\pi)}$.
Completing the elementary real square in (7) gives constants $c_1,C_1>0$
such that

$$
|F_N(\theta+iy)|
 \le A_N\exp\!\left(N[F_*-c_1u^2+C_1y^2]\right).\tag{10}
$$

Shrink $\eta_0$ once. In fixed disks about $\theta=0$ and $\theta=2\pi$ the same
function and any fixed finite number of its derivatives are bounded by
$\operatorname{poly}(N)A_Ne^{N(F_*-\gamma_0)}$ with $\gamma_0>0$. One may prove this either
by Cauchy on a still smaller fixed disk or by differentiating the explicit
chirp and applying Cauchy to the child. These endpoint disks are far from
$\theta=\pi$; their fixed positive angular loss exceeds all sufficiently small
height costs. The statement includes complex endpoints, not just their
real values.

The function $F_N$ has equal endpoint values and is symmetric under
$F_N(2\pi-\theta)=F_N(\theta)$. Its first derivative jump is

$$
F_N'(2\pi)-F_N'(0)=i\varepsilon N F_N(0).
$$

Set $\psi(\theta)=\theta(2\pi-\theta)$,

$$
b_N=-\frac{i\varepsilon N F_N(0)}{4\pi},\qquad
G_N(\theta)=F_N(\theta)-b_N\psi(\theta).\tag{11}
$$

Then $G_N,G_N',G_N''$ have matching endpoint values: the first two by
construction, the last by the reflection symmetry. Its periodic extension
is $C^2$ and piecewise analytic. It has Fourier coefficients

$$
g_{N,k}=\frac1{2\pi}\int_0^{2\pi}
 G_N(\theta)e^{-ik\theta}\,d\theta.
$$

with $g_{N,k}=O_N((1+|k|)^{-4})$. This follows by four integrations by parts,
retaining the finite third-derivative jump. Consequently the series for G
and G' converge absolutely, and substituting them into (6) is legitimate:

$$
Z_{N,h}(G)=(-1)^hN^2
 \sum_{m\in\mathbb Z}(-1)^m(m+1)g_{N,h+mN}.\tag{12}
$$

The correction $b_N\psi$ has nodal functional bounded by
$\operatorname{poly}(N)A_Ne^{N(F_*-\gamma_0)}$. It is not discarded; it will be added
back at the end.

For $k>0$ shift the coefficient contour to $\operatorname{Im}\theta=-\eta$; for $k<0$ shift to
$+\eta$, where $0<\eta\le\eta_0$ is fixed. Both vertical joining sides must remain.
Their difference has the form

$$
D_N(y)=G_N(2\pi-iy)-G_N(-iy),\qquad k>0.
$$

or its upper-half counterpart. By (11), $D_N(0)=D_N'(0)=D_N''(0)=0$.
Its first three y derivatives on the fixed joining interval have the
endpoint-gap bound above. Three integrations by parts in
$\int_0^\eta e^{-|k|y}D_N(y)\,dy$ yield the explicit upper bound

$$
\operatorname{poly}(N)A_Ne^{N(F_*-\gamma_0)}
 \left[e^{-|k|\eta}\bigl(|k|^{-1}+|k|^{-2}+|k|^{-3}\bigr)
                +|k|^{-4}\right].
$$

The lower-limit terms vanish because the three stated endpoint jets
match. The upper-limit terms are precisely the retained joining-current
terms. The shifted horizontal edge is bounded using (10), and the
subtracted quadratic has the smaller endpoint exponent. Thus, after
adjusting a polynomial factor independent of k,

$$
|g_{N,k}|\le\operatorname{poly}(N)A_N
 \left[e^{N(F_*+C_1\eta^2)-|k|\eta}
       +\frac{e^{N(F_*-\gamma_0)}}{(1+|k|)^4}\right],
\qquad k\ne0.\tag{13}
$$

For $h\ge\delta N$ and $0\le h\le d$, every NONZERO-weight frequency $h+mN$ in
(12) has absolute value at least $\delta N$. This uses $m=-1$ having zero
weight. The exponentially decaying terms sum to at most a fixed multiple
of $e^{-\delta N\eta}$; the inverse-fourth-power terms are absolutely
summable after multiplication by $|m+1|$. Choose fixed eta small enough
that $C_1\eta^2<\delta\eta/2$. Equations (12),(13) and the correction bound
give (9), reducing the positive margin to absorb $\log A_N=o(N)$ and
polynomial factors. All choices precede $N\to\infty$. No contour height
is allowed to grow with N, and no endpoint current is omitted.

## 6. Actual all-s root-star source theorem and its remaining boundary

The independent input is now proved and fully cross-reviewed in
[the full-jet star localization theorem](actual_conway_root_star_full_jet_localization.md),
§§1–8. For every
fixed $s\ge2$, take the literal expression

$$
\begin{aligned}
Z_N(j_0,\ldots,j_s)
 &=\phi\!\left(h_{j_0}^{\varepsilon_0}
          T\!\left(\prod_{i=1}^s h_{j_i}^{\varepsilon_i}\right)\right),\\
h_j^\varepsilon&=T(R^\varepsilon L_j).
\end{aligned}
$$

Every leaf is independent. Every $1\le j_i\le N$ and $\varepsilon_i\in\{0,+1,-1\}$
is allowed. This is a whole original source, not an equal-color restriction.
Put $G_0=g(1/4)=2\operatorname{Catalan}/\pi$ and $F_*=2sG_0$.
Here $M=\lfloor(N-1)/2\rfloor$, $s_r=\prod_{v=1}^r2\sin(\pi v/N)$,
$s_0=1$, $J(u)=\int_0^u\log(2\sin\pi v)\,dv$, and
$g(u)=J(2u)-4J(u)$.

The cited input proves (7) for the WHOLE physical child product, uniformly
in all those colors and signs. Its source-exact proof uses:

$$
\widehat B_r(-w-w^{-1})
 =\sum_{\ell=0}^{2r}
 \frac{s_{2r}}{s_r^2s_\ell s_{2r-\ell}}\,w^{r-\ell},
 \qquad0\le r\le M.\tag{14}
$$

with strictly positive Laurent coefficients; polynomially conditioned
full Hermite interpolation; a polynomial bound on the first normals
of ALL high Newton coordinates; and the actual core/alias coefficients.
The unique joint core-envelope maximum is $(r/N,\theta)=(1/4,\pi)$.
Logarithmic Taylor expansion gives the negative angular quadratic there;
a strict arc-rearrangement inequality and uniform moving-zero logarithm
bounds control its complement. The whole high alias has a strict rate
loss even after its full normal data are included. This proves (7) on
a fixed complex strip, not merely on real nodes.

Moreover, in the full-jet norm used in that proof, every child alias has
rate at most $2G_0-\Delta$, where $\Delta=G_0-v_3/\pi>0$, every whole child has
rate at most $2G_0$, and a child with $N-j_i\ge\delta N$ has a uniform strict
loss. The unturned physical root $R^\varepsilon L_j$ has polynomial jet norm.
Those facts give strict losses for all sectors containing a child alias,
and for every physical-color complement in a child, uniformly in the
ROOT color and sign.

The remaining sector in this proof is the root alias with all children
unrestricted. Its exact form is, up to the original sign,

$$
\phi\!\left(R^{\varepsilon_0}L_h
                  \prod_{i=1}^s h_{j_i}^{\varepsilon_i}\right),
\qquad1\le h\le\lfloor N/2\rfloor.
$$

In (9) the complementary index is $N-h\ge N/2$. Hence that ENTIRE contraction
has a fixed strict loss below $F_*$. No absolute value has been inserted
inside its root Fourier sum. The missing $m=-1$ term is decisive, because
it removes the potentially small mode -h.

To spell out the sector bookkeeping, write each full child as core plus
alias and let $E_{\mathrm{core}}$ be the product of its core factors. Then

$$
\begin{aligned}
Z_{\mathrm{full}}-Z_{\mathrm{all\text{-}core}}
 &=\phi\!\left(\mathrm{root}_{\mathrm{alias}}T(E_{\mathrm{full}})\right)\\
 &\quad+\phi\!\left(\mathrm{root}_{\mathrm{core}}
                  T(E_{\mathrm{full}}-E_{\mathrm{core}})\right).
\end{aligned}
$$

The first summand has the root-character loss just proved. The second
has at least one child alias. By (1), its root factor becomes
$T(\mathrm{root}_{\mathrm{core}})$, the difference of the two
physical unturned circle coupons used by the exact core/alias identity;
its jet cost is still polynomial. Expanding finitely many child factors
therefore gives a fixed $\gamma_{\mathrm{alias}}>0$ with

$$
|Z_{\mathrm{full}}-Z_{\mathrm{all\text{-}core}}|
 \le e^{N(F_*-\gamma_{\mathrm{alias}})}.\tag{15}
$$

uniformly over every physical color tuple and half-twist pattern, for
all sufficiently large N. For the same reason, (9) plus the child-color
jet loss gives, for every fixed $\delta>0$,

$$
\max_i(N-j_i)\ge\delta N
 \quad\Longrightarrow\quad
 |Z_{\mathrm{full}}|\le e^{N(F_*-\gamma_\delta)}.\tag{16}
$$

The preliminary complete bound is $|Z_{\mathrm{full}}|\le e^{N(F_*+o(1))}$.
All statements include both parities and composite levels.

The reference is exactly the original complete action. At all pure
complete colors,

$$
\begin{aligned}
Z_N(N,\ldots,N)&=\phi(L_Nh_N^s)
       =N\sum_{k=0}^{N-1}h_N(c_k)^s>0,\\
\lim_{N\to\infty}\frac1N\log Z_N(N,\ldots,N)&=2sG_0.
\end{aligned}\tag{17}
$$

The last assertion follows from the actual positive Newton expansion:
$\log\widehat B_r(-2)=Ng(r/N)+O(\log N)$, so the maximizing index is quarter.
For odd N the node -2 is present. For even N use the closest node and
$r=\lfloor N/4\rfloor$; all its relevant factors stay away from zero, and the
$O(N^{-2})$ node shift changes that single term by only $O(N^{-1})$ in logarithm.
This is a genuine every-level lower bound, not an upper-only normalization.

There are $H=s+1\ge3$ literal leaves. The complete star has inner leaf
labels 1/4 and root label $\arctan(s)/\pi$. At each inner prefix the exact port
is $(B,X,Y)=(1/r,1,1/r)$, so every retained gate is strict. The original
wire lattice still has $K=2H-3$ coordinates. The reviewed [general all-core and quarter-packet argument](actual_conway_general_core_packet_and_gap.md)
uses the strict gate Hessians and the high/quarter source theorems; it
provides the unique complete all-core maximum, its state complement gap,
and the original nonzero local $N^{3/2}$ packet with all offsets and phases.
Equations (15),(16) restore that packet to the WHOLE physical star source.
The stronger local spectral packet in the independent child proof is
consistent with this original wire packet but is not needed to replace it.

This is a source theorem. Applying a whole-filling theorem additionally
requires the original marked geometric deformation and full Fourier-period
interfaces, with their fixed-slope and knot-component hypotheses. No tangle
isotopy or new filling normalization is claimed in this derivation.

For arbitrary completed E with internal turns, (1)--(6) remain exact,
and (7)--(13) remain a valid sufficient implication. This note DOES NOT
claim that such E satisfies (7) at its original geometric exponent.
The high Newton part of a general turned child is not determined by its
node values; silently replacing it by a semisimple quotient would lose
precisely the normal contribution in (4). That broader spectral
localization is the remaining general task.

## 7. Independent review of the pre-existing envelope obstruction

The following elementary calculation explains why a separate positive
root-alias envelope does not suffice.
For C(h T(h^s)), a=$\arctan(s)/\pi$ and $X=1/s$. If $s\ge8$, the elementary
Ti_2/atan inequalities give $\pi g(a)<37/48$, while
$k(a)\ge\operatorname{Catalan}/\pi>8/(9\pi)$. Hence

$$
k(a)-g(a)>\frac{17}{144\pi}>\frac{119}{3168}.
$$

The last inequality uses $\pi<22/7$. This is only failure of a proposed
positive upper bound to certify a gap, not a lower bound on the signed
alias or a counterexample to a volume limit. The correlated Fourier
contraction above avoids applying that separate root envelope.

## Internal review and validation scope

The primary reviewer read the entire source, Fourier and contour proof,
including the actual star assembly, with analytical PASS. An independent
coherent-source reviewer rederived the residue weights, missing frequency,
normal-coordinate formula, calibrated chirp, endpoint repair, both joining
currents and their summation; the full proof and source scope received PASS.
The child localization input received a separate full source/analytical
review, and the general all-core packet input was independently checked.
These are internal analytical reviews, not external peer review or formal
verification. Native mathematical rendering and relative-link validation
are preservation checks. No numerical asymptotic experiment is used.
