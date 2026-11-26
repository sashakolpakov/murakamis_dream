# Full source propagation after the first three-crossing entrance

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The proved first entrance belongs to a larger source class that is
preserved by the full Fourier attachment. The proof combines the
original central contour with absolute bounds on every complementary
input interval. Consequently it propagates a nonzero original-source
coefficient, rather than only an analytic critical phase.

## 1. The class and the exact attachment

Use the original matrices and cardinal vector, and put
\[
 A_N=JM^3,\qquad
 \widetilde A_N=A_N-E_{\lfloor N/40\rfloor},\qquad
 K_N(x,y)=h(x)^T\widetilde A_Nh(y),\qquad
 x_h=\frac16+\frac{i\log2}{2\pi}.
 \tag{1}
\]
Keep the original kernel phase \(\Phi\), nonzero amplitude
\(a_K\), and unit carrier \(\kappa\). Set
\[
 \begin{gathered}
 R=1/200,\quad W=9/1000,\quad L=1/50,\quad
 H_*=57/10000,\quad b=9/50,\quad A=29/20,\quad a=3/2,\\
 \mathcal U=\{|z|\le R\}\cup[-W,W],\qquad
 v(t)=\min\{\operatorname{dist}(t,\mathbb Z),3/100\},\\
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),\quad K=|k_0|,\quad
 \rho=\frac{5-\sqrt{21}}2,\quad D=5+\sqrt{21},\\
 Z=\frac{(21/20)\rho}{1-(3/10)\rho},\qquad
 C_0=\frac{K(D+3/5)}{2(D-3/5)^2}.
 \end{gathered}
 \tag{2}
\]
An incoming source is an actual finite half-band function, with the
period sign \((-1)^{N-1}\) of \(h\), satisfying
\[
 \begin{split}
 F_N(x_h+z)&=\omega_N N^\nu f(z)e^{NS(x_h+z)}(1+O(N^{-1})),
       \qquad f(z)\ne0,\quad z\in\mathcal U,\\
 S'(x_h+z)/k_0&=-\sqrt{21}z+g(z),\qquad
 |g(0)|\le H\le H_*,\qquad |g'|\le b,\\
 |F_N(x_h+t)|&\le CN^q
 e^{N[M+KHv(t)-Av(t)^2]},\qquad t\in\mathbb R,
       \quad M=\Re S(x_h).
 \end{split}
 \tag{3}
\]
The packet is uniform and holomorphic on a neighborhood of the closed
union, with a holomorphic normalized remainder and its fixed
derivatives on smaller neighborhoods. The unit factor \(\omega_N\)
is retained. The number \(H\) is a certified upper bound, not
necessarily the exact central derivative magnitude.

The actual attachment is the entire original horizontal period
\[
 F_{N,+}(y)=N\int_{x_h-1/2}^{x_h+1/2}F_N(x)K_N(x,y)\,dx.
 \tag{4}
\]
If \(F_N(x)=\ell_N^TB_Nh(x)\), the bilinear cardinal identity
gives exactly
\[
 N\int h(x)h(x)^T\,dx=I,
 \qquad F_{N,+}(y)=\ell_N^TB_N\widetilde A_Nh(y).
 \tag{5}
\]
Thus (4) retains the finite word, its original first normals and both
level parities. It does not introduce a Hermitian pairing or replace
an ordinary outside color by a Fourier endpoint.

## 2. The full induction theorem

**Theorem 1.** The source class (3) is preserved by (4). More
precisely, let \(z_c(w)\) be the selected critical point of
\(S(x_h+z)+\Phi(x_h+z,x_h+w)\), and set
\[
 S_+(x_h+w)=S(x_h+z_c(w))
                 +\Phi(x_h+z_c(w),x_h+w).
 \tag{6}
\]
Then the full original source has the nonzero packet
\[
 \begin{split}
 F_{N,+}(x_h+w)
 &=\omega_N\kappa N^\nu f_+(w)
        e^{NS_+(x_h+w)}(1+O(N^{-1})),\\
 f_+(w)
 &=\frac{\sqrt{2\pi}\,f(z_c(w))
                 a_K(x_h+z_c(w),x_h+w)}
 {\sqrt{-[S''+\Phi_{xx}](x_h+z_c(w),x_h+w)}}\ne0,
                  \qquad w\in\mathcal U.
 \end{split}
 \tag{7}
\]
The Gaussian square root is the branch with positive real part.
The outgoing derivative bounds and full real envelope in (3) hold
with \(H_+=ZH\), \(M_+=\Re S_+(x_h)\), and unchanged
\(\nu,A,v,b\). The conclusion iterates for every fixed number
of attachments. Uniform holomorphic parameter versions of the input
hypotheses give the same assertion with fixed parameter derivatives.

*Proof.* The [larger analytic phase theorem](research_three_larger_phase_class.md)
constructs the unique critical branch and preserves the derivative
class. Its sharper outgoing estimates are \(|g_+'|<.16\) on
the disk and \(<.15\) on the real interval. It retains the exact
normalization
\[
 |S_+(x_h)-S(x_h)-2c|\le C_0H^2,\qquad
 |g_+(0)|\le ZH.
 \tag{8}
\]
These facts concern the actual phase and its additive constant.

All required kernel inputs have already been proved for the literal
source (1). The [union-domain packet](research_three_vertex_real_input_union.md)
applies for real input \(|t|\le L\), with output in
\(\mathcal U\). The bidisk packet and the exact symmetry
\(K_N(x,y)=K_N(y,x)\) supply complex input in the true disk
and output in either part of the union. The
[two-wire real theorem](research_three_vertex_two_wire_large_cap_bound.md)
and [joint height theorem](research_three_vertex_large_cap_height_bound.md)
supply the original global bounds, respectively
\[
 \begin{split}
 |K_N(x_h+t,x_h+u)|&\le CN^q
       e^{N[2c-a\{v(t)^2+v(u)^2\}]},\qquad t,u\in\mathbb R,\\
 |K_N(x_h+t,x_h+w)|&\le CN^q
       e^{N[2c+13(\Im w)^2-a\min\{d_{\mathbb T}(t,0),.04\}^2]},
       \quad |w|\le R.
 \end{split}
 \tag{9}
\]
The second is a joint angle-height assertion, not the sum of two
unrelated bounds.

Partition the original input period at \(\pm R,\pm W,\pm L\).
The following proved estimates exhaust it:

| Input region | Original-source estimate |
|---|---|
| \([-R,R]\) | Exact deformation to the two segments through \(z_c\); nonzero full Gaussian coefficient |
| \(R\le |t|\le W\) | Absolute action loss \(>1/80000\) |
| \(W\le |t|\le L\) | Absolute action loss \(>1/100000\) |
| \(L\le d_{\mathbb T}(t,0)\le1/2\) | Absolute action loss \(>1/2500\) |

Each loss is relative to \(\Re S_+(x_h+w)\), uniformly on
the output union. The first, second and fourth rows are proved in
[the central and outer transport theorem](research_three_generic_source_outer_transport.md).
Its central contour lies entirely inside the incoming source disk;
the two endpoint rays lie in opposite Gaussian convergence sectors.
No separate half-contributions or omitted vertical currents occur.
The third row is
[the intermediate-annulus theorem](research_three_larger_source_intermediate_annulus.md).
For real output it compares with the actual phase at \(z=\rho w\)
before estimating the residual. For disk output it uses the exact
quadratic completion at \(W\). The original kernel curvature
then extends both comparisons through \(L\). In particular no
cubic estimate is extrapolated beyond its proved domain, and the
incoming source is never evaluated on a complex complementary annulus.

The finite central deformation is exact by holomorphy with fixed
endpoints. Its original packets and the accretive wire Hessian
give (7) with relative error \(O(N^{-1})\). The complementary
bounds are absolute and exponentially smaller, so cannot cancel
that coefficient. The Gaussian square root is single-valued because
\(-\Re(S''+\Phi_{xx})>18\) on the central contour. The original
powers are
\[
                  N\cdot N^\nu\cdot N^{-1/2}\cdot N^{-1/2}=N^\nu.
 \tag{10}
\]
The carriers multiply by exactly \(\kappa\).

It remains to reset the real-period envelope. Let
\(C=C_0+K^2/[4(A+a)]\). The first estimate in (9), input square
completion and (8) imply, on the whole outgoing real period,
\[
 |F_{N,+}(x_h+u)|\le CN^q
       e^{N[M_++CH^2-a v(u)^2]}.
 \tag{11}
\]
For \(v(u)\ge W\), the outer transport theorem proves
\[
 CH^2\le KZH W+(a-A)W^2
         \le KZH v(u)+(a-A)v(u)^2,
                 \qquad 0\le H\le H_*.
 \tag{12}
\]
The first comparison follows from convexity in \(H\) and its
two endpoint checks; at \(H_*\) its reserve exceeds
\(.00001061\). Keeping the nonnegative certified outgoing
linear term \(KZH v\) is essential. For \(|u|\le W\),
the newly proved packet and the outgoing derivative bound give
\[
 \Re S_+(x_h+u)
 \le M_++KZH|u|
 -\frac12\{\sqrt{21}\Re k_0-Kb\}u^2
 \le M_++KZH|u|-Au^2.
 \tag{13}
\]
This supplies the remaining envelope. Equations (7), (12) and (13)
prove preservation of every part of (3).

All domains are compact and the gaps are strict. For uniformly
holomorphic input parameter families the same proof works on a
smaller fixed neighborhood, and Cauchy estimates give the fixed
ordinary derivatives. For any fixed number of attachments, these
neighborhoods and constants may be reduced finitely many times;
no uniformity for a length growing with \(N\) is claimed.
\(\square\)

## 3. The actual entrance and the small closing class

The [proved first-entrance real extension](research_three_first_entrance_real_extension.md)
supplies precisely the actual complete-ended source
\[
 F_N^{[3]}(y,w)=v(w)^TA_N^3h(y),\qquad w=-2,
 \quad \nu=-1,\quad \omega_N=C_{N,3}\kappa^2,
 \quad H_0=.0057,
 \tag{14}
\]
with the packet and envelope (3), including its original ordinary
complete boundary. Thus the entrance hypothesis is realized; it is
not an unproved preparation condition in this application.

**Corollary 2.** For every fixed integer \(j\ge0\),
\[
 F_N^{[3+j]}(y,-2)=v(-2)^TA_N^3\widetilde A_N^{\,j}h(y)
 \tag{15}
\]
has a nonzero packet on the output union, power \(N^{-1}\),
carrier \(C_{N,3}\kappa^{2+j}\), actual iterated phase,
and the full real envelope (3) with \(H_j=Z^jH_0\).
The total change from homogeneous action increments is bounded by
\[
 \left|S_j(x_h)-S_0(x_h)-2jc\right|
 \le C_0H_0^2\sum_{r=0}^{j-1}Z^{2r}
 \le\frac{C_0H_0^2}{1-Z^2}<6\cdot10^{-6}.
 \tag{16}
\]
The actual iterated action is retained in the exponential; (16)
does not replace it by a homogeneous action.

Every fixed ordinary derivative at the complete outside color is
retained in (15) and in its whole-period envelope, with a possibly
larger polynomial factor in \(N\). Here the assertion is about
actual ordinary jets, not a fixed off-color envelope. The explicit
input is [the wider prepared-source theorem](research_three_prepared_cap_real_extension.md),
Corollary 4 and Proposition 3: every fixed ordinary derivative has
the same real-period and far-arc exponential bounds. Differentiating
the exact first-entrance integral therefore gives these same bounds
for the entrance (14). Its local holomorphic packet supplies the
differentiated principal term. More precisely, with ordinary parameter
\(\lambda=0\) at the complete color, the induction transports
\[
 \partial_\lambda^\beta F_N(x_h+z,0)
 =\left.\partial_\lambda^\beta
   [\omega_NN^\nu f(z,\lambda)e^{NS(x_h+z,\lambda)}]
   \right|_{\lambda=0}
 +O\!\left(N^{\nu+|\beta|-1}e^{N\Re S(x_h+z,0)}\right),
\]
uniformly on the internal union, together with the global bounds
for each fixed jet at the same exponential rate as the base source.
The phase and amplitude here are their analytic critical-transform
germs; an off-color envelope is not part of this jet assertion.
At each subsequent step differentiate
(4) before integrating; the kernel is independent of that outside
color. All complementary estimates apply to the differentiated
incoming source with only polynomial changes. On the central contour,
differentiate the original local stationary-phase expansion, retaining
its polynomial-in-\(N\) amplitude factors. This gives exactly the
ordinary derivatives of the phase and coefficient in (7). It does
not assert that an individual derivative has a nonzero leading term.
Induction proves the fixed-jet assertion without inferring any
off-color exponential bound from a value estimate at \(-2\).

After two attachments,
\[
 Z^2(.0057)<.000312<1/2500.
 \tag{17}
\]
The resulting source therefore enters the already proved
[small-source class](research_three_source_tail_propagation.md):
restrict the packet to the disk, and weaken its distance cap from
\(.03\) to \(.01\). Indeed \(KHv-Av^2\) decreases for
\(v\ge.01\) when \(H\le1/2500\), so the larger-cap envelope
implies the required smaller-cap one. This gives actual finite
entrance into the source class used by the
[full bilinear closing theorem](research_three_small_source_closure.md).

This corollary establishes the original-source propagation at complete
outside color and its fixed ordinary jets. The parameter version of
Theorem 1 applies whenever
the corresponding source bounds are supplied uniformly nearby.
Closing two such sources, calibrating their critical action with
marked geometry, and restoring the exact Fourier corners are separate
proved operations with their own hypotheses; they are not replaced
by (16) or by an assumption about a homogeneous Fourier boundary.

## 4. Reproduction and computational scope

Run

```sh
python3 experiments/check_three_larger_source_propagation.py --precision 192
```

The [assembly checker](../experiments/check_three_larger_source_propagation.py)
and [record](../repro/results/research-three-larger-source-propagation.json)
check the exact period partition, numerical class inclusions, finite
normalization and word orientation, and the provenance of the passed
component checks. The contour proofs and their original-source
coefficients remain the written arguments cited above. No frozen
manuscript or knot-identification claim is changed by this note.
