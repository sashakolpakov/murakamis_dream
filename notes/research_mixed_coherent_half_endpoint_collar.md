# A coherent collar beyond the real half-period

Research deduction, 5 November 2026. This extends the restricted original
integral across the half-period endpoint by an unquantified positive
width. The width comes from already proved complete-source neighborhoods
and compact derivative bounds. No new interval cover is used. Neither a
specified right-half interval nor a whole-period asymptotic follows.

## 1. Complete finite sources on the required neighborhoods

Fix the collar parameter \(0<\rho\le1/1000\) in the exact
[periodic hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
Let \(\phi_{\eta\epsilon}\), \(g\), \(J=\Re g\), and the
original selected finite integrals have the normalization of the
[deep-low half-region theorem](research_mixed_deep_low_half_region.md).
In particular, no conditional row, Fourier factor, or carrier is changed.

The following inputs concern the original finite canonical sum, not just
its critical root or a formal continuation of an asymptotic error.

* [Complex stability of the real packet](research_mixed_real_packet_complex_stability.md),
  Theorem 1, gives its full uniform packet on an **open complex neighborhood**
  of every compact real set in \((0,1/2]^2\), including
  \([\rho,1/2]^2\). Its Sections 2--4 directly control both midpoint
  currents, both aliases, the exterior zero mode and the moving central
  saddle, including the zero-height transition.
* [The left/right interface packet](research_mixed_left_right_interface_source.md),
  Theorem 1, gives the full packet on open neighborhoods of each
  \(T_\eta\times W_\epsilon\) and reversed product. Here \(T\)
  is the original early cap, and each right triangle \(W\) contains
  the real vertex \(1/2\).
* [The full right-square packet](research_mixed_unselected_right_taper_products.md),
  Theorem 1, gives open neighborhoods of the independent products
  \(B_3=[.22,.50]+i[-.03,.02]\) and
  \(B_4=[.22,.50]+i[-.057,.0141]\). Its source assertion includes
  both selected and unselected allowed heights; only its subsequent
  comparison theorem restricts to unselected heights.

Consider a target pair on the old graph with at least one real coordinate
equal to \(1/2\). That target has height zero. If the other real coordinate
is at least \(.1\), its target is in its early cap or in its right-square
rectangle. If it is below \(.1\), both targets are real and belong to
\([\rho,1/2]^2\). Thus the finite list of compact slices
\[
 T_\eta\times\{1/2\},\quad B_\eta\times\{1/2\},\quad
 [\rho,.1]\times\{1/2\},\quad\text{and their reversals}
 \tag{1}
\]
is covered by the preceding open complete-source neighborhoods, for
every type pair. The point \((1/2,1/2)\) is included.

Choose a smaller open neighborhood of (1) with compact closure inside
those source neighborhoods. Original zero-lift roots, actions and
nonzero symbols agree on overlaps: they are the same calibrated branch
of the same finite canonical source. Shrink further if necessary to
keep every critical factorial argument in its original regular strip.
Compactness supplies \(d_0\in(0,1/10)\) such that replacing either
half-endpoint argument by a real point of \([1/2,1/2+d_0]\)
stays in these neighborhoods, including simultaneous replacements.
The full packet and the original factorial divisions remain uniform
there. This is the finite-source justification for the extension.

Let \(D_\rho<\infty\) bound both
\(|\partial_a\phi_{\eta\epsilon}|\) and
\(|\partial_b\phi_{\eta\epsilon}|\) on this smaller compact
neighborhood, for every type pair. It may be replaced by any larger
positive number. No numerical value is asserted. Set
\[
 K_\rho=2D_\rho+\log2,\qquad
 0<\delta_\rho<\min\{d_0,\,1/(4000K_\rho)\}.
 \tag{2}
\]
The domains in (1) and these constants depend on \(\rho\), but not
on the length or type word. Finite prefactors below may depend on the
fixed word.

## 2. The true Fourier correction beyond one half

For \(x\in[1/2,1/2+d_0]\), the hybrid target is real and its
height is zero. The original Fourier upper rate is
\(\max\{-J(x),0\}=0\), since
\[
 J(1/2)=0,\qquad J'(x)=\log(2\sin\pi x),\qquad
 0\le J(x)\le(x-1/2)\log2.
 \tag{3}
\]
The last inequalities hold because \(d_0<1/10\). A selected factor
\(X^{-N}\) has modulus one on this real segment.

The allocated phase \(\phi\) already includes the factorial Fourier
rate \(-J\). Therefore the actual upper rate must add \(J(x)\)
at **every type-four coordinate beyond one half**, whether selected or
unselected. Each incident edge supplies one half of this correction;
the total is a full \(J(x)\), also for a loop. A relative approximation
to \(d_N\) is not used on this segment: its forcing alternative is
essential.

For a target \(x\in[\rho,1/2+\delta_\rho]^m\), put
\[
 R_x=\{j:x_j>1/2\},\qquad \bar x_j=\min\{x_j,1/2\},
 \qquad \bar S=S\setminus R_x.
 \tag{4}
\]
Changing \(x_j>1/2\) to \(1/2\) leaves its height zero and every
neighboring height unchanged: both slow and fast left cutoffs equal one
throughout the change, and the own right factor is zero. Removing its
selection changes no height either. This includes repeated incidences
at periods one and two. Consequently the clamped point is exactly the
old hybrid target for \((\bar x,\bar S)\).

Writing \(z=z_S(x)\), the full upper phase is
\[
 \widetilde{\mathcal E}_S(x)=\Re\sum_j\phi_j(z_{j-1},z_j)
  +\sum_{j\in S\setminus R_x}\max\{\Re g(z_j),-2\pi\Im z_j\}
  +\sum_{j\in R_x}\epsilon_jJ(x_j).
 \tag{5}
\]
Here \(\epsilon_j=1\) means type four. Formula (5) keeps the actual
Fourier forcing bound and every selected frequency. All other original
blocks use the already established bounds on their unchanged targets.

Move the coordinates in \(R_x\) successively to their clamped values.
Every affected pair stays in the compact neighborhoods from Section 1.
The two incidences of each coordinate and (3) give
\[
 \widetilde{\mathcal E}_S(x)
 \le\mathcal E_{\bar S}(\bar x)
            +K_\rho\sum_{j\in R_x}(x_j-1/2).
 \tag{6}
\]
For a one-cycle, the derivative of the single diagonal action is the
sum of its two partial derivatives, so its bound is \(2D_\rho\),
not a duplication of the original edge. For a two-cycle the two edges
retain their literal multiplicities.

## 3. The existing boundary loss pays for the collar

Let \(M\) be the actual geometric critical rate. The deep-low
half-region theorem gives
\(\mathcal E_{\bar S}(\bar x)\le M-\sum_j\omega_j(\bar x,\bar S)\),
where
\[
 \omega_j(y,\sigma)=\frac1{4000}
  \min\{1,\sigma_j+400(\operatorname{clamp}_{[.22,.45]}(y_j)
                    -\Re r_j)^2\}
     +\frac{(y_j-.45)_+}{10}.
 \tag{7}
\]
At a clamped coordinate \(\bar x_j=1/2\), its removed selection
does not erase this loss. The reference bound \(\Re r_j<.39\)
implies saturation of the minimum in (7), and
\[
 \omega_j(\bar x,\bar S)=\frac1{4000}+\frac1{200}
                  =\frac{21}{4000}.
 \tag{8}
\]
Equations (2), (6) and (8) prove the pointwise bound
\[
 \boxed{\widetilde{\mathcal E}_S(x)
  \le M-\sum_{j\notin R_x}\omega_j(x,S)-\frac{|R_x|}{200}.}
 \tag{9}
\]
No tangent extrapolation or assertion about monotonicity of individual
finite rows is involved. The collar coordinate comparison spends only
a compact derivative bound against a previously proved strict loss.

Let \(P=[.22,.45]\). Outside the unselected plateau contribution,
(9) gives a phase loss of at least \(1/4000\): either \(R_x\)
is nonempty, or the original occupation bound applies. For each fixed
word, choose the Fourier tolerance on each of its \(m\) allocated
blocks below \(1/(8000m)\). The complete source packets, the unchanged
polynomial normalization, and the bounded exact hybrid Jacobian give
\[
 \left|\mathcal Z_N^{\rm hyb}([\rho,1/2+\delta_\rho]^m)
       -\mathcal I_{N,\varnothing}^{\rm hyb}(P^m)\right|
 \le C N^A\exp N(M-1/8000)
 \tag{10}
\]
at all sufficiently large levels of either parity. Thus this larger
restricted integral retains the original central coefficient, carrier
and level power. The comparison map (4) is not used as an integral
substitution; both sides of the region decomposition use the original
graph and differential form.

The positive width in (2) is not quantified. In particular this argument
does not cover the diagnostic interval reaching approximately .575,
does not supply a uniform width as \(\rho\downarrow0\), and does not
bound the remaining full-period complement or any boundary insertion.

```sh
python3 experiments/check_mixed_coherent_half_endpoint_collar.py
```

The focused checker binds the completed open-source and phase inputs
and checks the forcing and reserve arithmetic. It does not compute
\(D_\rho\), \(d_0\), or \(\delta_\rho\), and performs no new cover.
