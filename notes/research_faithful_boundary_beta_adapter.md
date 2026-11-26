# A faithful boundary packet for the first actual beta move

Written proof, 23 November 2026. The retained cyclic factorial in the
first actual nine-cell beta move can be removed with zero error on a
faithful boundary packet. For a positive crossing this packet is one
complete middle-degree row; for a negative crossing it is one complete
middle-degree column. Explicit continuants reconstruct the whole original
Hopf box, including every repeated-root normal, from that packet.

Reconstruction is part of the assertion. The ratio-free array alone is
not asserted to be the original crossing. After reconstruction the boxes
can be substituted in any fixed literal Conway construction, with its
original turns, marked closing, pivots and external scalar lines. This
does not require a nonzero knot invariant or a semisimple quotient.

The algebraic reconstruction works at every level \(N\ge2\). Its literal
charged nine-cell application has the existing odd-level scope \(N>2\).
No positive gluing formula, tame reconstruction norm, geometric source
coefficient, or volume lower bound is proved.

## 1. The complete physical algebra and its source

Put
\[
 N\ge2,\qquad d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 x=-q^{-1}=q^d,\qquad F_j=(Q;Q)_j.
 \tag{1}
\]
All physical head indices lie in \(0,\ldots,d\). Square brackets mean
reduction to that set; physical total degree below is an ordinary
integer, not a residue. Let \(V\) have its original balanced basis.
The generators are
\[
 E|a\rangle=(Q^{-a}-1)|a-1\rangle,\quad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\quad
 K|a\rangle=xQ^{-a}|a\rangle,
\]
with outside-basis arrows omitted.
The original pair Casimir and complete Hopf algebra of [P] are
\[
 E_t=E_1K_2+E_2,\qquad F_t=F_1+K_1^{-1}F_2,\qquad K_t=K_1K_2,
 \qquad \Omega=F_tE_t+qK_t+q^{-1}K_t^{-1},
\]
\[
 H_N=\mathbb C[z]/P_N(z),\qquad
 P_N(z)=2T_N(z/2)+2=\prod_{j=0}^d(z-c_j),\qquad
 c_j=q^{2j+1}+q^{-2j-1}.
 \tag{2}
\]
Here the \(F_t,F_1,F_2\) in the coproduct denote quantum-group arrows,
not the scalar factorials \(F_j\) of (1). The physical representation
\[
                    f\longmapsto f(\Omega)
 \tag{3}
\]
identifies \(H_N\) with the entire two-head \(E_t,F_t,K_t\) commutant.
These are the actual operators, including the derivative channels at
double roots of \(P_N\). Here normals mean the Casimir directions
\(f'(c)\) at those double roots. All parameters stay at (1); no moving
meridian family or quantum-parameter jet is asserted.

Let
\[
 W_d=\operatorname{span}\{e_j=|j,d-j\rangle:0\le j\le d\},
 \qquad A=\Omega|_{W_d}.
 \tag{4}
\]
By [P,H], \(A\) is complex symmetric and irreducible tridiagonal:
\[
 A_{jj}=a_j,\qquad A_{j,j+1}=A_{j+1,j}=b_j=-(1-Q^{j+1})^2.
 \tag{5}
\]
Every \(b_j\) is nonzero. Its characteristic and minimal polynomial are
both \(P_N\). Thus restriction of (3) to \(W_d\) remains faithful.
No eigenvector diagonalization is used below.

The original fixed-root closing is
\[
 \phi(f)=\frac1N\operatorname{Tr}_{V\otimes V}
                  [(I\otimes g)f(\Omega)]
        =(-1)^dN^2[z^d]\operatorname{rem}_{P_N}f
        =(f(A))_{0d},
 \qquad g=K^{1-N}.
 \tag{6}
\]
This endpoint identity is for a complete Hopf box. It is not asserted
for an arbitrary matrix inserted into the pivotal trace.
The actual turn \(J\) is the full linear involution on \(H_N\), with
its original cups and caps. In the normalized Newton basis
\[
 e_r^{\rm N}(z)=s_r^{-2}\prod_{h<r}(c_h-z),\qquad
 s_r=\prod_{h=1}^r2\sin(\pi h/N),\qquad s_0=1,
 \tag{7}
\]
it obeys \(Je_r^{\rm N}=e_{d-r}^{\rm N}\). The two original rows are
\[
 \lambda_0(f)=f(c_0),\qquad \phi(f)=\lambda_0(Jf).
 \tag{8}
\]
Any separately recorded framing, peripheral or closing multiplier is
retained outside these identities.

## 2. Two faithful observations and their explicit inverses

For a matrix \(Y\) on \(W_d\), define its first-row and last-column data
\[
 \rho_+(Y)=(Y_{0j})_{j=0}^d,\qquad
 \rho_-(Y)=(Y_{id})_{i=0}^d.
 \tag{9}
\]
Both observations are defined on every matrix, without a Hopf condition.
Their restrictions to \(\mathbb C[A]\) are isomorphisms onto
\(\mathbb C^N\).

Here is an explicit proof and inverse. Define the monic continuants
\[
 p_0(z)=1,\qquad p_1(z)=z-a_0,\qquad
 p_{j+1}(z)=(z-a_j)p_j(z)-b_{j-1}^2p_{j-1}(z),
 \tag{10}
\]
and
\[
 B_0=1,\qquad B_j=\prod_{h=0}^{j-1}b_h=(-1)^jF_j^2,\qquad
                         u_j(z)=p_j(z)/B_j.
 \tag{11}
\]
The recurrence is used up to \(j=d-1\). Every denominator is nonzero.
Induction in (10), applying the tridiagonal matrix to \(e_j\), gives
\[
                         p_j(A)e_0=B_je_j.
 \tag{12}
\]
Indeed it holds for \(j=0,1\). If it holds at \(j,j-1\), the
\(e_{j-1}\) terms cancel, and the remaining term is
\(B_jb_je_{j+1}=B_{j+1}e_{j+1}\).
Since \(A\) is symmetric, (12) also gives
\[
                         e_0^{\mathsf T}u_j(A)=e_j^{\mathsf T}.
 \tag{13}
\]
All transposes in this proof are bilinear transposes, without conjugation.
Consequently the first-row inverse is the polynomial
\[
             I_+(w)=\sum_{j=0}^dw_ju_j(z)\quad\bmod P_N.
 \tag{14}
\]
Its degree is at most \(d\), and its first physical row is exactly \(w\).
Uniqueness follows either from (12) or because the \(u_j\) have distinct
degrees \(j\) and nonzero leading coefficients.

For the opposite endpoint reverse the coefficients:
\[
 \widehat a_j=a_{d-j},\qquad \widehat b_j=b_{d-1-j}.
 \tag{15}
\]
Let \(\widehat p_j,\widehat B_j,\widehat u_j\) be given by
(10),(11) with these coefficients. The same induction gives
\[
 \widehat u_j(A)e_d=e_{d-j},\qquad
                     I_-(v)=\sum_{i=0}^dv_i\widehat u_{d-i}(z).
 \tag{16}
\]
Thus \(I_-(v)(A)e_d=v\), with all output entries retained.

Define full physical completions of arbitrary middle-degree matrices by
\[
 \mathcal P_+(Y)=I_+(\rho_+(Y))(\Omega),\qquad
 \mathcal P_-(Y)=I_-(\rho_-(Y))(\Omega).
 \tag{17}
\]
They are linear maps into the complete Hopf algebra. They fix every
\(f(\Omega)\), since their selected row or column agrees with it.
Equivalently, their restrictions back to \(W_d\) are retractions onto
\(\mathbb C[A]\). Formula (17) also specifies all other physical degrees;
they are not filled by arbitrary matrices.

These observations are faithful to normals. If all observed entries
of \(f(A)\) vanish, (14) or (16) forces \(f=0\) in \(H_N\).
In particular no nonzero double-root derivative direction is discarded.
This conclusion uses the full minimal polynomial, not values only at
the distinct \(c_j\). The original cup, in contrast, is an eigenvector:
\(f(\Omega)p=f(c_0)p\). That one column does not replace (9).

## 3. The actual nine-cell port maps

For the charged-array application suppose now that \(N>2\) is odd.
Write the strict signed crossings of [R] as \(M_\sigma^0\), where
\[
             R_+=\kappa M_+^0,\qquad
             R_-=\kappa^{-1}M_-^0,\qquad
             \kappa=q^{d^2/2}.
 \tag{18}
\]
The \(R_\pm\) are the full original physical crossings and are inverses.
All fractional powers mean the original specified exponentials.
Both \(M_\sigma^0\) are complete Hopf boxes preserving integer degree.

Use the original eight boundary face indices and their four differences
\[
 k_m=\alpha_{m,-}-\alpha_{m,+}+h_m,\qquad
 f_m(k)=s_{0m}^{[k-1]}s_{m5}^{[-k]},\qquad 1\le m\le4.
 \tag{19}
\]
The \(h_m\) are the original charges; the \(s_{ab}\) are the specified
nonzero decoration roots. They are not new adjustable normalizers.
Keep the literal scalar \(C_N(\mathbf s)\), and put
\[
             \varphi_+=3(h_1-1)/2,\qquad \varphi_-=0.
 \tag{20}
\]
These are the original sector conventions of [R].

The exact positive port map is
\[
 \mathcal E_+(M)_\alpha
 =C_NQ^{\varphi_+}s_{05}^dN^2Qx^{b-u}
        \prod_{m=1}^4f_m(k_m)\,M_{v,u;a,b},
\]
\[
 u=[-k_1],\quad v=[-k_2],\quad
 a=[k_3-1],\quad b=[k_4-1].
 \tag{21}
\]
The negative port map is instead
\[
 \mathcal E_-(M)_\alpha
 =C_NQ^{\varphi_-}s_{05}^dN^2x^{b-e}
        \prod_{m=1}^4f_m(k_m)\,M_{c,e;a,b},
\]
\[
 c=[-k_1],\quad e=[-k_4],\quad
 a=[k_2-1],\quad b=[k_3-1].
 \tag{22}
\]
The different index placement and the extra positive \(Q\) are retained.
Equations (21),(22) are the literal maps of [R,(17),(18)].

For middle-degree output \((i,d-i)\) and input \((j,d-j)\), define
\[
 \mathbf k_+(i,j)=([i+1],[-i],[j+1],[-j]),\qquad
 \mathbf k_-(i,j)=([-i],[j+1],[-j],[i+1]).
 \tag{23}
\]
Their complete nonzero port scalars are
\[
 e_{+,ij}=C_NQ^{\varphi_+}s_{05}^dN^2Qx^{i-j}
                         \prod_mf_m(k_{+,m}(i,j)),
\]
\[
 e_{-,ij}=C_NQ^{\varphi_-}s_{05}^dN^2x^{i-j}
                         \prod_mf_m(k_{-,m}(i,j)).
 \tag{24}
\]
On the regular decoration domain each is a unit.
For any boundary array let its paired-fiber average at \(\mathbf k\)
mean \(N^{-4}\) times the sum over all face indices satisfying (19).
There are exactly \(N^4\) such indices. In particular (21),(22) give
\[
 \left\langle\mathcal E_\sigma(M)\right\rangle_{\mathbf k_\sigma(i,j)}
                         =e_{\sigma,ij}M_{i,d-i;j,d-j}.
 \tag{25}
\]
Thus division by the actual \(e_{\sigma,ij}\), after this specified
average, is the port inverse used here. No norm bound for that inverse
is asserted.

## 4. Delete the ratio on the faithful packet

The first beta identity in [R,(30)--(32)] has a distinguished quotient
\[
 \frac{\overline W_{0235}(K+L)}
      {\overline W_{0235}(K+L-k_2)}.
 \tag{26}
\]
For reference its five remaining internal indices can be called
\(u,v,\tau,s,z\in\mathbb Z/N\), with
\[
 K=u+v+1,\qquad L=1-k_1+s+z,\qquad
 \Xi_0=u(1+\tau)+v(1+s)+(1+\tau)(1+s)
                       +z-k_1+(3h_1-1)/2.
 \tag{27}
\]
Besides (26), its base-sector internal weight is precisely
\[
 \mathfrak n\mathfrak f_{01235}Q^{\Xi_0}
 \frac{W_{1234}(u)W_{1245}(v)W_{2345}(\tau)
              W_{0134}(s)W_{0145}(z)}
 {\overline W_{1235}(K)\overline W_{0135}(L)
              \overline W_{0345}(k_4+\tau+v+z)}.
 \tag{28}
\]
This is the literal beta image of the boundary coefficient in
(21),(22), with every boundary multiplier still attached.
In particular \(\mathfrak n,\mathfrak f_{01235},C_N\), the sector phases
and the \(f_m\) factors are not reset to one. Factors already present
in (21),(22) are not multiplied a second time. For the negative or
another transported sector retain its original extra boundary phase
once, as prescribed in [R, Section 6].

The bar on \(W\) is a label, not complex conjugation. In normalized
Fermat coordinates its recurrence is
\[
 \frac{\overline W(n+1)}{\overline W(n)}
        =\frac{\beta}{1-\alpha Q^n},\qquad
 \alpha^N+\beta^N=1,\qquad \alpha\beta\ne0.
 \tag{29}
\]
All roots are the original jointly marked roots. Their products are
periodic. Explicitly \(W(n)=\prod_{h=1}^{[n]}\beta/(1-\alpha Q^h)\)
and \(\overline W(n)=\prod_{h=0}^{[n]-1}\beta/(1-\alpha Q^h)\),
with both empty products equal to one; scalar decoration factors
remain in (28). In the present quotient put
\[
 m=[-k_2],\quad r_0=u+v+s+z+2,\quad t=\alpha_{0235}Q^{r_0}.
 \tag{30}
\]
Since \(K+L=r_0-k_1\) modulo \(N\), (29) gives exactly
\[
 \frac{\overline W_{0235}(K+L)}
      {\overline W_{0235}(K+L-k_2)}
 =R_m(tQ^{-k_1}),\qquad
 R_m(Z)=\beta_{0235}^{-m}(Z;Q)_m.
 \tag{31}
\]
In particular it equals one whenever \(k_2=0\), for every internal
tuple. This does not identify the internal \(r_0\) with a boundary index.

Define the ratio-free beta coefficient by replacing only (26) by one
in this literal finite beta sum. Retain all of (27),(28), all original
port factors and the same paired-fiber average. Denote the resulting
paired coefficient by \(\mathfrak b_\sigma^\flat(\mathbf k)\).
This is a specified finite tensor operation, not a new invariant.
Equivalently it is the paired average of the literal beta array with
that single quotient deleted. Only these paired coefficients are needed.

Before deletion the corresponding coefficient is
\(\langle\mathcal E_\sigma(M_\sigma^0)\rangle_{\mathbf k}\):
this is the actual finite beta identity of [R]. That identity retains
arbitrary exterior coefficients, and hence applies coefficientwise to
these paired coefficients. Since (26) is identically one at \(k_2=0\),
\[
 \mathfrak b_\sigma^\flat(\mathbf k)
   =\left\langle\mathcal E_\sigma(M_\sigma^0)\right\rangle_{\mathbf k}
                         \quad\text{if }k_2=0.
 \tag{32}
\]
No cancellation or sign estimate has been used in this equality.

Pull the ratio-free coefficients back to a middle-degree matrix:
\[
 (Y_\sigma^\flat)_{ij}
     =e_{\sigma,ij}^{-1}
                 \mathfrak b_\sigma^\flat(\mathbf k_\sigma(i,j)).
 \tag{33}
\]
For the positive sign, \(\mathbf k_+(0,j)=(1,0,[j+1],[-j])\).
For the negative sign, \(\mathbf k_-(i,d)=([-i],0,1,[i+1])\).
Equations (25),(32),(33) therefore prove the entire row and column
identities
\[
 \rho_+(Y_+^\flat)=\rho_+(M_+^0|_{W_d}),\qquad
 \rho_-(Y_-^\flat)=\rho_-(M_-^0|_{W_d}).
 \tag{34}
\]
There are \(N\) observations in each identity, not a single cup value.

## 5. Exact reconstructed boxes and arbitrary Conway assembly

**Theorem.** On the regular marked decoration domain, at every odd
\(N>2\), the literal ratio-free beta packets satisfy
\[
 \boxed{\qquad
 \mathcal P_+(Y_+^\flat)=M_+^0,\qquad
 \mathcal P_-(Y_-^\flat)=M_-^0.
 \qquad}
 \tag{35}
\]
Consequently the full original signed crossings are
\[
 \boxed{\qquad
 R_+=\kappa\mathcal P_+(Y_+^\flat),\qquad
 R_-=\kappa^{-1}\mathcal P_-(Y_-^\flat).
 \qquad}
 \tag{36}
\]
**Proof.** By (34), each reconstructed box and its original Hopf box
have identical faithful data (9). The uniqueness established in
(12)--(17) proves equality in \(H_N\), hence on the full physical pair.
The scalar factors in (18) prove (36). This argument includes every
normal at every repeated root. \(\square\)

For clarity, (35) is not an equality
\(Y_\sigma^\flat=M_\sigma^0|_{W_d}\). Unobserved rows or columns can
change upon deletion. Reconstruction is the explicit kernel (17),
and is retained once at every replaced crossing.

Now take any fixed literal Conway expression with signed crossing
leaves, products in \(H_N\), genuine turns \(J\), and its original closing
row. Replace each signed leaf by the corresponding right side of (36).
Induction over the expression shows that every open subtree packet
is unchanged: this is true at the leaves by (36), preserved by the
same product, and preserved by the same linear turn. Applying the
same original closing therefore gives exactly the same scalar.
Pivots, framing and peripheral lines retain their original positions
and values. No equality for a modified non-Hopf array is inserted
in place of (6).

Integer twist leaves can be reconstructed internally and multiplied
before substitution into the original expression. Thus arbitrary fixed
short powers and all other prescribed powers are included as finite
identities at each level. There is no large-twist hypothesis here.
This is an exact source adapter, not a statement about their asymptotics.

If reconstruction is moved to an exterior covector, its full bilinear
dual must be moved there. It is not removed by a metric change or by
replacing that covector with an endpoint row. The same rule applies to
the inverse port factors (24). Individual ray-modified crossing patterns
need their actual transported co-source from [R]; (36) concerns the
original complete crossings, not a new endpoint closing for those
individual patterns.

## 6. Norms and the unchanged degree-four minimum

The sparse original signed data help identify the cost still present.
By [H, Section 3], the first middle-degree row of \(R_+\) has only its
last entry nonzero, equal to \(\kappa x^{-d}\).
Inverting this row identity gives
\[
                       R_-e_d=\kappa^{-1}x^d e_0.
 \tag{37}
\]
Indeed \(e_0^{\mathsf T}R_+=\kappa x^{-d}e_d^{\mathsf T}\)
implies \(e_d^{\mathsf T}R_-=\kappa^{-1}x^d e_0^{\mathsf T}\);
symmetry supplies (37). Thus both selected data vectors in (36),
with their full Cartan factors restored, have Euclidean norm one.
The other observed beta entries vanish by the full signed finite sum.
They are not independent positive summands.

In the Newton norm from (7), the complete original packets are [C]
\[
 R_\pm=\kappa^{\pm1}
             \sum_{r=0}^d(-q)^{\pm r}e_r^{\rm N},\qquad
                         \|R_\pm\|_{\rm N}=\sqrt N.
 \tag{38}
\]
Accordingly the inverse on these particular actual data has norm ratio
\(\sqrt N\) into this specified packet norm. This is not an operator
bound for (17) on arbitrary data, a physical Hilbert--Schmidt bound,
or a bound for changing the metric of further gluing. The continuant
and port kernels retain their entire physical cost and complex phase.

There is also a precise consequence for the degree-four source minimum
of [C]. Keep the same literal compiler, Newton metric, vertices, local
tensors \(T_v\), original root row and budgets
\[
 b_v=16\max(1,\|T_v\|_{\rm HS}),\qquad B_{\rm tot}=\prod_vb_v.
 \tag{39}
\]
If a prescribed leaf packet is replaced by its exactly reconstructed
beta expression, the resulting element of \(H_N\) is the same leaf.
Hence every \(T_v\), every \(b_v\), and every normalized recursion
\(\Phi_v\) is unchanged. On the identical product of unit balls the
objective remains pointwise
\[
 E_N(x)=|Lx_{v_0}|^2+
             \sum_v\|\Phi_v((x_c)_c)-x_v\|^2.
 \tag{40}
\]
Its gradient, minimum and [C]'s value
\((197/196)B_{\rm tot}^2\min E_N\) are therefore exactly unchanged,
including at zeros. This does not assign old budgets to a new enlarged
network of ratio-free variables and reconstruction gates.

The gain proved here is zero-error removal of the retained ratio on
a faithful full-normal packet, followed by exact original-source
assembly. General interpolation, cyclic-row reconstruction and the
existence of algebra projections are existing tools. Their application
to this actual beta quotient and its two signed port placements is the
source-specific content. The reconstruction kernel still carries
coherent complexity. No geometric trial, positivity, subexponential
full inverse, or volume lower bound follows.

## Complete inputs and closest coverage

The complete matching texts used for the proof are:

- [R] [Full-Psi ray crossings and the original nine-cell boundary](research_full_psi_ray_crossings_and_nine_cell_boundary.md), 588 lines, SHA-256 495a2fde1ed1d7ca0707f060208121bddb2673be21ff3bcb9bac737420ac2d24.
- [P] [Full physical pair commutant and marked trace](actual_pair_casimir_commutant_and_rotated_trace.md), 331 lines, SHA-256 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666.
- [H] [Complete Casimir--Hermite packets](actual_complete_casimir_hermite_packet.md), 321 lines, SHA-256 a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.
- [C] [Strongly convex minimum for the complete Conway source](research_convex_normalized_conway_source.md), 329 lines, SHA-256 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c.

R supplies the literal port maps, complete finite beta identity and
its co-source scope. P supplies the full algebra, physical tridiagonal
block, genuine turn and original closing. H supplies the existing
continuants and sparse signed row; the reconstruction proof is written
out above. C fixes the Newton normalization and the exact compiler used
in (38)--(40). No additional eigenframe or Gram inverse is assumed.

Two complete closest comparisons were read for coverage:

- [Source-preserving commutant projection and window repair](research_source_preserving_commutant_projection_and_window_repair.md), 543 lines, SHA-256 ff75410cfbba220c17bfd8153f27f901f21f1d98077b186945ebe502f24032e2.
- [Original crossing in the coupled flag Euler exchange](research_actual_crossing_flag_euler_exchange.md), 287 lines, SHA-256 784a76132cf8116ec8afc5807e6bd98bb51178beb7f959b7ce3ab42e56eab6b5.

The first constructs a different lowering-commutant projection calibrated
to one source functional, rather than the faithful beta completion (17).
The second transports the full retained coupon in coupled flags; it
does not perform its elimination on a faithful row or column.
Only written mathematics and text/hash operations were used.
