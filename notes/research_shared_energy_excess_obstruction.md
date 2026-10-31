# The shared spectral energy can exceed the complete volume rate

31 October 2026. **Reviewed research result; not approved for publication.**
On one certified original seven-port source, the endpoint-conditioned
energy exceeds the complete rate by more than 0.50, already at one
fixed real spectral corner. This disproves the stronger proposed bound

$$
\sup_{\boldsymbol\sigma\in[-2,2]^R}E_{\mathrm{NC},N}
\le \exp\{N(\Phi_D+o(1))\}.
$$

It does not refute the weaker endpoint-mass budget or the joint shared-flow
criteria in the [energy theorem](general_endpoint_conditioned_source_energy.md).
It is not a lower bound for the original oscillatory invariant.

## 1. An exact original shared flow

Take the width-three word

$$
[1,3,0,2,4,1,3]
$$

with the first cap marked. The original compiler gives protected faces
$0,6$, ordinary faces $1,2,3,4,5,7,8$, and the seven ordered quartets

$$
\begin{split}
&(1,0,4,2),\ (2,0,5,3),\ (0,1,6,4),\ (4,2,7,5),\\
&(5,3,8,0),\ (6,4,0,7),\ (7,5,0,8).
\end{split}\tag{1}
$$

Select only port $2$ as RIGHT; the other six ports are CROSS. At that
port the outer $x=0$ and opposite middle $c=6$ are protected. Its
normalized exponents have the form

$$
q_x=q_c=0,\qquad q_y=w,\qquad q_b=1-w,\qquad 0<w<\tfrac12.
\tag{2}
$$

By the literal reflection of the
[protected-outer coefficient theorem](actual_protected_outer_spectral_energy.md),
its actual coefficient and reference entropies satisfy

$$
k^*(q)=0,\qquad h_0(q)=-2f(w),\qquad
2k^*(q)-h_0(q)=2f(w)=C(0,\tfrac12-w,w).
\tag{3}
$$

Here $C(\alpha)=\sum_j f(\alpha_j)$, $\sum_j\alpha_j=1/2$, and

$$
f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}\pi.
$$

Equation (3) is an actual energy rate, not merely the general local upper
bound. Its weighted energy potential is

$$
\Psi_R=\tfrac12\log L_1+Q(0,L_1,L_4).
\tag{4}
$$

The flow therefore consists of the original input triangle $(0,1,4)$
of supply $1/2$, and a fixed half-unit at face $1$. This is entropy
bookkeeping for (2); it introduces no new finite coupon or changed mark.

The [registered certificate](../experiments/research_shared_energy_excess_obstruction_certificate.json)
contains 30 exact rational corner values on the 13 original triangle
rows other than port $2$'s output row $(0,6,4)$. Every row sums to
$1/2$. With the fixed half-unit at face $1$, every ordinary face receives
exactly one and both protected faces receive zero. At all six CROSS ports,
both middle degrees are strictly less than $1/2$; at port $2$, the
$b$-degree is strictly greater than $1/2$. All these assertions are
checked over the rationals against the original compiler.

Put

$$
E_{\mathrm{cert}}=\sum_{\text{13 registered rows}}C(\alpha_{\mathrm{row}}).
\tag{5}
$$

At a CROSS port its two registered rows give one allowed split of the
outer degrees, so their entropy is at most the actual coefficient entropy.
At the selected port its one row gives exactly (3). No numerical optimizer
is used to justify either assertion.

## 2. Actual integer arrays and a fixed spectral corner

Let $q_{e,f}$ be the aggregated rational port-face flow above. For each
even $N=2m$, set $d=N-1$. On the original port-face transportation
network give each incidence the integer bounds

$$
\lfloor d q_{e,f}\rfloor\le v_{e,f}\le\lceil d q_{e,f}\rceil.
\tag{6}
$$

The fractional flow $dq$ satisfies these bounds and all integer port
supplies $d$ and ordinary face demands $d$. Integrality of the bipartite
transportation network gives an integer flow $v_N$ between the bounds.
All zero incidences, including the protected ones, remain exactly zero,
and $v_N/d\to q$.

The fixed strict middle slack gives $v_b,v_c\le m-1$ at each CROSS port
for all sufficiently large even $N$, and $v_b\ge m$ at the RIGHT port.
These are the actual finite supports with the true target $d=N-1$.
The [full positive endpoint kernel](actual_fejer_full_kernel_entropy_identity_reduction.md)
contains every degree-$d$ monomial, and its CROSS part has precisely these
middle inequalities. Thus the original central factor is retained by
classification of the actual coefficient. No separate rounding of formal
half-triangle rows or removal of a forced outer factor is used.

At the six CROSS ports choose $\sigma_e=-2$. At even levels the original
reference is $p_N(v)=-a_N(v;-2)>0$, and hence

$$
\frac{|a_N(v;-2)|^2}{p_N(v)}=p_N(v)
\tag{7}
$$

exactly. At the selected port use the fixed value $\sigma_2=+2$.
After literal row reflection its monomer starts at $i=0$. Writing
$\theta=\pi/N$, the exact unused-row formula and $\chi_N(2)=4$ give

$$
|a_N(v;2)|=
\csc^2(\theta/2)
\prod_{r=1}^{j}
\left[\frac{\sin(r\theta)}{\sin((r+1/2)\theta)}\right]^2,
\qquad j\le m-1.
\tag{8}
$$

Sine increases throughout these arguments. The unsquared product is
between $\sin\theta/\sin((j+1)\theta)$ and $1$, including $j=0$.
Consequently

$$
4\cos^2(\theta/2)\le |a_N(v;2)|\le\csc^2(\theta/2).
\tag{9}
$$

Its rate at this fixed spectral value is zero. The uniform endpoint
entropy therefore yields the selected-port energy rate in (3), at the
actual rounded exponents.

Let

$$
\boldsymbol\sigma^*=(-2,-2,+2,-2,-2,-2,-2).
$$

The positive shared energy contains the summand indexed by $v_N$.
The uniform closed endpoint coefficient theorem, (3), and (7)--(9) imply

$$
\boxed{\displaystyle
\liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}
\frac1N\log E_{\mathrm{NC},N}(\boldsymbol\sigma^*)
\ge E_{\mathrm{cert}}.}
\tag{10}
$$

All spectral coordinates belong to the same original shared numerator.
No spectral optimization, limit/supremum exchange, or independent local
face contraction is used.

## 3. A certified excess over the complete rate

For an independent complete upper bound use the fixed ordinary radii

$$
(L_0,\ldots,L_8)=(0,16,9,25,1,4,0,1,9).
\tag{11}
$$

The [actual complete capacity formula](actual_smoothed_source_capacity_blocks.md)
gives, simply by evaluating one positive ordinary vector,

$$
\Phi_D\le U=
\sum_{\text{14 original triangles}}Q(L_{\mathrm{triangle}})
-\sum_{f\ \mathrm{ordinary}}\log L_f.
\tag{12}
$$

This vector is also the original complete packing, but its optimality is
unnecessary for the upper bound (12).

The [verify-only audit](../experiments/audit_research_shared_energy_excess_obstruction.py)
uses the fixed rational certificate and Arb arithmetic at 192 bits.
Each Lobachevsky Fourier series has 8192 terms and the explicit
absolute tail $1/(2M)$. The [registered results](../experiments/research_shared_energy_excess_obstruction_results.json)
prove

$$
E_{\mathrm{cert}}>7.51209890188,\qquad
U<6.99858850313,\qquad
E_{\mathrm{cert}}-\Phi_D>0.50.
\tag{13}
$$

The certified excess lower endpoint is greater than 0.51351039.
Equations (10)--(13) refute the stronger energy-at-most-complete-rate
proposal on an actual certified original source. The even subsequence
already suffices to refute an all-level upper bound.

## 4. The weaker criteria are unaffected

For a sector with endpoint mass rate $z_s$ and energy rate $e_s$, the
weaker Cauchy condition is $z_s+e_s<2\Phi_D$. This certificate does not
compare the energy excess with the endpoint mass loss and does not
disprove that condition.

The joint score must retain both terms on the same original flow. At
the selected doubly protected port, (3) gives exactly

$$
\frac{h_0(q)+g(q)}2=0=k^*(q).
\tag{14}
$$

The positive energy rate compensates an exponentially small reference
coefficient; it is not positive growth of the original spectral
coefficient. The universal joint-score and combined-envelope inequalities
remain open. No lower bound for the original oscillatory source, no
failure of its volume limit, and no obstruction to the weaker energy
budget follows from this counterexample.

## 5. Review and verification scope

The private proof and exact verifier received full independent analytical
reviews from the root and cluster agents. Cluster also completed a fresh
redirected Arb replay. The fixed-corner sine-product strengthening (8)--(9)
received a separate independent analytical review. The portable verifier
preserves the reviewed `verify` function's complete syntax tree and the
registered certificate bytes; only imports and output/default paths were
changed. It has no optional numerical builder or optimizer dependency.

Its finite checks establish the original incidence, rational feasibility,
support slack, and certified entropy inequalities. The asymptotic step
uses the proved uniform coefficient theorems and integer transportation
argument; no sampled large-level rate is presented as proof.
