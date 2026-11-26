# The original turn in the half-charge coupon norm

Private written corollary, 17 November 2026.

The product-trace estimate [Q] applies to identified ordinary
coupon slots. Gluing two output slots through an original turn
uses a different bilinear pairing. Its literal exterior kernel
has exponential rate \(M_\infty\) in that estimate's norm,
even though the norm retains Gaussian weights on first normals.
This is a cost of that particular upper-bound method, not an
asymptotic assertion about a contracted source.

## 1. The exact two gluing operations

Use the original full Hermite algebra and pairing of [C]:
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad D=N-1,
\]
\[
 \phi_N(e_i e_j)=\delta_{i+j,D},\qquad
 \mathsf T e_i=e_{D-i},\qquad
 K_N(z,w)=\sum_{i=0}^{D}e_i(z)e_i(w).
 \tag{1}
\]
The turn is an involution and is self-adjoint for this
bilinear Frobenius pairing. These assertions follow on the
basis in (1), and hence with arbitrary ordinary spectator
polynomials as coefficients.

Let \(f,g\in\mathcal A_N\) be two input states and let their
output states be \(F=\mathsf T f\), \(G=\mathsf T g\).
Then the original turn joining the inputs is
\[
 \begin{split}
 \phi_N(f\,\mathsf T g)
 &=\phi_N(F\,\mathsf T G)\\
 &=(\phi_N^{(z)}\phi_N^{(w)})
                  [F(z)K_N(z,w)G(w)].
 \end{split}
 \tag{2}
\]
In contrast, identifying the output variables and multiplying gives
\[
                         \phi_N(FG)=\phi_N(fg).
 \tag{3}
\]
In Newton coefficients the two pairings on the inputs are,
respectively, \(\sum_i f_i g_i\) and
\(\sum_i f_i g_{D-i}\). Thus (3) cannot replace (2).
All identities are in the full algebra, with every required
normal and all spectator couplings retained.

In particular, for the literal coupon of [Q], put
\[
 C_{r,n,N}(z,\zeta_2,\ldots,\zeta_r)
 =\phi_N^{(x)}
   [R(x)^n A(x)K_N(x,z)\prod_{i=2}^{r}K_N(x,\zeta_i)],
 \qquad A=e_{N-1-\lfloor N/2\rfloor}.
 \tag{4}
\]
The reproducing identity in [C] gives exactly
\[
 \boxed{\quad
 \mathsf T_z[C_{r,n,N}]
   =[R(z)^nA(z)\prod_{i=2}^{r}K_N(z,\zeta_i)]
       \quad\hbox{in }\mathcal A_N^{(z)}.
 \quad}
 \tag{5}
\]
For \(r=1\) the right side is \([R^nA]\).
The other variables in (5) remain ordinary and unreduced.
It is an equality of the full traced \(z\)-jet class, not an
ordinary off-grid polynomial identity in \(z\). Ordinary
derivatives in the other variables commute with it.

## 2. The precise exterior norm

Write \(m=\lfloor N/2\rfloor\), \(J_N=\lfloor(N-1)/2\rfloor\), and
\[
 c_a=2\cos((2a+1)\pi/N),\qquad
 \tau_a=\arccos(-c_a/2),\qquad g_a=1-\cos\tau_a.
 \tag{6}
\]
The multiplicity \(\mu_a\) of \(c_a\) is two, except for the
odd simple node \(c_m=-2\), where it is one.
For a fixed \(c>0\), the \(\mathbf q=(1,1)\) instance of
[Q, (7)] is
\[
 \|E\|_{N,c,(1,1)}
 =\max_{\substack{0\le a,b\le J_N\\
                  0\le\beta<\mu_a,\ 0\le\gamma<\mu_b}}
 |\partial_z^\beta\partial_w^\gamma E(c_a,c_b)|
                 e^{-cN(\beta g_a+\gamma g_b)}.
 \tag{7}
\]
In particular every value row has weight one. Only its
prescribed normal rows receive these weights.

**Theorem.** For every fixed \(c>0\),
\[
 \boxed{\qquad
 \lim_{N\to\infty}N^{-1}\log\|K_N\|_{N,c,(1,1)}
       =M_\infty=\frac{4G}{\pi},
 \qquad}
 \tag{8}
\]
where \(G=\int_0^{\pi/4}\log\cot u\,du\).
The limit is along both parities with the same normalization.

**Proof of the upper bound.**
First set \(U=m-1\) and
\[
                    K_N^<(z,w)=\sum_{j=0}^{U}e_j(z)e_j(w).
 \tag{9}
\]
At the \(m\) double nodes its grid values equal those of
\(K_N\). For \(j\le a\), the Newton product has
\[
 0\le e_j(c_a)\le e_j(-2),\qquad e_j(c_a)=0\quad(j>a).
 \tag{10}
\]
Consequently, at those double-node pairs,
\[
 0\le K_N^<(c_a,c_b)=F_{a,N}(c_b)
       \le F_{a,N}(-2)\le F_{J_N,N}(-2),
 \tag{11}
\]
where \(F_{a,N}(w)=K_N(c_a,w)\).
The last inequality is the actual positive-row inequality
[S, (8)]. The all-row estimate [S, (6)] gives
\[
                       F_{J_N,N}(-2)\le CN^B e^{NM_\infty}.
 \tag{12}
\]
Indeed its normalized profile is
\[
 \Psi_x(-2)=\int_0^x2\operatorname{arsinh}(\cot\pi s)\,ds
       \le\Psi_{1/2}(-2)=M_\infty.
 \tag{13}
\]
The equality in (13) follows by
\(\operatorname{arsinh}\cot u=\log\cot(u/2)\).

The double-node cardinal polynomials in [S, (22)] have
polynomial real-interval norm. Tensor interpolation of
the degree-\(U\) polynomial (9) in both variables therefore
extends (11)--(12) to all of \([-2,2]^2\) at polynomial cost.
At even levels this is the entire low kernel.
At odd levels the additional low term is \(e_m(z)e_m(w)\).
Here, by the exact distinct-root product,
\[
 e_m(z)=\frac{(-1)^m}{N}
                  \{U_m(z/2)-U_{m-1}(z/2)\},\qquad
                         \|e_m\|_{[-2,2]}\le1.
 \tag{14}
\]
Thus the same bound holds for the low kernel at both parities.
The remaining radical kernel has real-cube norm at most
\(m(N-1)\) by [H, (34)--(36)]. Adding it proves
\[
                \|K_N\|_{[-2,2]^2}\le CN^{B'}e^{NM_\infty}.
 \tag{15}
\]
Its degree in each variable is \(D\). Tensor Markov
inequalities give the same exponential rate, at polynomial
cost, for every derivative used in (7). All weights in (7)
are at most one, proving the upper bound in (8).

**Proof of the lower bound.**
At odd levels choose \(a=b=J_N=m\), so both colors are
\(-2\). The value row in (7) gives
\[
                \|K_N\|_{N,c,(1,1)}\ge F_{J_N,N}(-2).
 \tag{16}
\]
At even levels choose \(a=b=J_N=m-1\), with
\(c_*=c_{J_N}=-2\cos(\pi/N)\). It gives
\[
                \|K_N\|_{N,c,(1,1)}\ge F_{J_N,N}(c_*).
 \tag{17}
\]
These values are positive. The full-row logarithmic theorem
[S, (7)] is uniform in \(0\le j\le J_N\) on any fixed
compact neighborhood of \(-2\) in the slit. Since
\(J_N/N\to1/2\) and \(c_*\to-2\), it yields
\[
 N^{-1}\log F_{J_N,N}(-2)\longrightarrow M_\infty,\qquad
 N^{-1}\log F_{J_N,N}(c_*)\longrightarrow M_\infty.
 \tag{18}
\]
Together (16)--(18) prove the lower bound, including the
even last-double-node channel. No nonexistent normal has
been added at the odd simple node. \(\square\)

## 3. Consequence and scope

If two coupon outputs are joined by an original turn, (2)
places \(K_N\) in the exterior of [Q]. Each of its two
variables has one coupon slot, so its norm is precisely
(7). Formula (8) shows that treating this exterior as
having zero exponential cost is invalid. The same conclusion
holds for every fixed choice of the Gaussian constant \(c>0\);
the lower bounds use unweighted value rows.

One can instead keep the exact turned state (5), including
its middle insertion and all other kernels. That is a
different input to subsequent estimates, not permission to
apply the unturned coupon bound to it.

The conclusion is not a lower bound for (2), does not
exclude cancellation there, and does not obstruct a joint
source proof for adjacent short fillings. It identifies
exactly which exterior estimate is unpaid by [Q].
Earlier real-norm unit-turn obstructions concern a different
map and norm; the statement here is the sharp rate of the
literal joining kernel in the new weighted full-jet norm.

## Complete direct sources

- Q: [Full traces of products of half-charge coupons](research_half_charge_coupon_product_trace_bound.md),
  SHA256 447dbd477941526ce56ddef6767715636401f621d7aaf1481bc9b9c22fa02ffe.
  The original coupon and the precise exterior norm.
- C: [Exact source compilation](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f.
  The full Frobenius pairing, turn kernel, and ordinary spectator convention.
- S: [Physical rows on the slit plane](research_mixed_next_first_short_edge_slit_plane_bound.md),
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
  Uniform actual-row logarithms, real normalization and finite cardinal bounds.
- H: [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
  The exact low/radical split and real-interval radical bound.

All four complete direct texts were read and their used implications
checked at these pins. Only written mathematics, text reads and hashes
were used. No mathematical program, test or build was run; frozen
notes and public manuscripts were unchanged.
