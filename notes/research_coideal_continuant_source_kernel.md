# An explicit coideal kernel with the original cup calibration

24 November 2026. Written research proof.

The actual conserved coideal admits polynomial kernel and cokernel
maps, including its collision parameters. A trailing continuant removes
the apparent inverse in their comparison. The original cup is the
image of an explicit endpoint seed; at the source-selected parameter
its spectral projection loses only a subexponential factor.
The original marked closing remains a specified row on this kernel.
No geometric cycle coefficient or scalar lower bound is inferred.

## 1. Actual matrices and continuants

Use the complete balanced physical basis of C and S. Put
\[
 N\ge2,\quad d=N-1,\quad b=2k\ge2,\quad
 q=e^{\pi i/N},\quad \sqrt q=e^{\pi i/(2N)},\quad
 Q=q^2,\quad x=-q^{-1},\quad
 F_a=(Q;Q)_a,\quad F_0=1,\quad F_d=N .
 \tag{1}
\]
The basis is orthonormal. The actual one-head generators have entries
\(Ke_a=xQ^{-a}e_a\), \(Ee_a=(Q^{-a}-1)e_{a-1}\), and
\(Fe_a=(1-Q^{a+1})e_{a+1}\), with both missing endpoint arrows zero.
For the ordered total generators define, as in C,
\[
 B_c=\mathsf F-(\mathsf E-cI)\mathsf K^{-1},\qquad
 T=B_c^{(b-1)},\qquad W=(\mathbb C^N)^{\otimes(b-1)} .
 \tag{2}
\]
Here \(c\) is an auxiliary parameter and \(B_c\) without a superscript
acts on \(V=\mathbb C^N\otimes W\). Its first-head tridiagonal action is
\[
 (B_cu)_a=(1-Q^a)u_{a-1}
       +q(1-Q^{a+1})u_{a+1}-qQ^aTu_a .
 \tag{3}
\]
Only indices \(0,\ldots,d\) occur. Write \(\iota_a:W\to V\) and
\(\pi_a:V\to W\) for coordinate insertion and extraction.

Let \(D_a(\lambda;T)\) be the leading continuant on indices
\(0,\ldots,a-1\) of \(\lambda I-B_c\), with \(T\) held fixed:
\[
 D_{-1}=0,\quad D_0=I,\qquad
 D_{a+1}=(\lambda+qQ^aT)D_a-q(1-Q^a)^2D_{a-1}.
 \tag{4}
\]
All its coefficients commute. Let \(E_d(\lambda;T)\) be the trailing
continuant on indices \(1,\ldots,d\), and \(D_{\rm mid}\) the one
on \(1,\ldots,d-1\); the empty determinant is \(I\).
The monic polynomial and exact identity from C are
\[
 p_N(z)=2q^{N/2}T_N\!\left(\frac{z}{2\sqrt q}\right),\qquad
 D_N(\lambda;T)=p_N(\lambda)-\gamma p_N(T),\quad
 \gamma=(-1)^{N+1}.
 \tag{5}
\]
Here \(T_N\) is Chebyshev of the first kind. Since \(b\) is even,
\(p_N(T)=\gamma^{b-1}p_N(c)\), so \(D_N(c;T)=0\).
Below, an omitted argument means \(\lambda=c\), \(T=B_c^{(b-1)}\).

## 2. A polynomial inverse valid at collisions

The tridiagonal determinant identity gives
\[
 D_dE_d-D_ND_{\rm mid}
        =\prod_{a=1}^dq(1-Q^a)^2=q^dN^2I .
 \tag{6}
\]
For clarity, the two cross-minors in the determinant identity are
the products of the upper and lower arrows. Their signs cancel and
give the displayed factor, including at \(N=2\).
Thus, on this actual tail module,
\[
 D_dE_d=q^dN^2I,\qquad
 D_d^{-1}=\frac{E_d}{q^dN^2},\qquad
 E_d^{-1}=\frac{D_d}{q^dN^2}.
 \tag{7}
\]
These are polynomial matrix identities in \(c\). No tail spectral
inverse or exclusion of collision parameters is needed.

Define the explicit rectangular maps
\[
 L_c=\sum_{a=0}^d\iota_a\,\frac{q^{-a}D_a}{F_a},
 \qquad
 M_c=\sum_{a=0}^d\frac{D_a}{F_a}\,\pi_a,\qquad Q_c=E_dM_c .
 \tag{8}
\]
The recurrence proves
\[
 (B_c-cI)L_c=0,\quad M_c(B_c-cI)=0,\quad
 \pi_0L_c=I,\quad M_c\iota_0=I .
 \tag{9}
\]
In particular \(L_c\) is a graph parameterization of the entire
\(c\)-eigenkernel, not a selection of particular eigenvectors.

There is an exact sequence at every \(c\):
\[
 0\longrightarrow W\xrightarrow{L_c}V
 \xrightarrow{\,B_c-cI\,}V\xrightarrow{M_c}W
 \longrightarrow0 .
 \tag{10}
\]
One can prove exactness without a dimension argument. The equations
in rows \(0,\ldots,d-1\) determine a kernel vector from its first
coordinate, using the nonzero upper arrows in (3).
For \(M_cw=0\), set \(z_0=0\) and solve
\((cI-B_c)z=w\) successively in those rows.
The remaining residual is supported at \(d\) and is killed by \(M_c\).
Its last coefficient \(D_d/F_d\) is invertible by (7), so that
residual is zero. The sign change to \(B_c-cI\) does not change its image.

This proof already works over \(\mathcal O_N[c]\), where
\(\mathcal O_N=\mathbb Z[\sqrt q,1/N]\).
Every \(1-Q^a\), \(1\le a<N\), is a unit there because their
product is \(N\). Equation (7) supplies the remaining unit.
Thus the kernel and cokernel are free of tail rank over this ring;
no field-rank argument or inversion of \(p_N'(c)\) enters (10).
Replacing \(M_c\) by \(Q_c\) gives the same exact sequence.

## 3. The finite kernel and its natural comparison

Put
\[
 r_c(z)=\frac{p_N(z)-p_N(c)}{z-c}.
 \tag{11}
\]
This is a monic polynomial of degree \(d\). The cofactor identity for
the tridiagonal matrix gives
\[
 \boxed{\qquad r_c(B_c)=L_cE_dM_c=L_cQ_c.\qquad}
 \tag{12}
\]
Here is an algebraic verification including collisions. The adjugate
of \(cI-B_c\), computed in the commutative coefficient ring generated
by \(T\), equals \(r_c(B_c)\) by (5) and Cayley--Hamilton.
Its columns lie in the kernel in (9), and its first row is a left
kernel row. Their first-coordinate normalizations are \(L_0=M_0=I\).
The \(00\) cofactor is \(E_d\), proving (12).

The exact normalization is
\[
 M_cL_c=\frac{p_N'(c)D_d}{q^dN^2},\qquad
                  Q_cL_c=p_N'(c)I .
 \tag{13}
\]
To check the derivative, first allow \(\lambda\) to vary with \(T\)
fixed. The recurrence gives
\[
 (\lambda I-B_c)L(\lambda)
             =\iota_d\,\frac{D_N(\lambda;T)}{q^dF_d}.
 \tag{14}
\]
Differentiate in \(\lambda\), evaluate at \(c\), and multiply by \(M_c\).
The term with \(L'\) vanishes by (9); \(M_c\iota_d=D_d/F_d\)
and \(D_N'(c;T)=p_N'(c)\) give (13), using (7).
This derivative is not differentiation of the tail \(T(c)\).

Consequently
\[
 r_c(B_c)^2=p_N'(c)r_c(B_c).
 \tag{15}
\]
When \(p_N'(c)\ne0\), \(r_c(B_c)/p_N'(c)\) is the spectral
projector onto \(\mathcal E_c=\ker(B_c-cI)\).
At a collision \(p_N'(c)=0\), (12) is instead a nonzero square-zero
map with image \(\mathcal E_c\) and kernel \(\operatorname{im}(B_c-cI)\).
Indeed \(L_c\) is injective and \(Q_c\) is surjective by (7)--(10).
The natural map from the kernel to the cokernel, using \(L_c,Q_c\),
is multiplication by \(p_N'(c)\). It vanishes at a collision.
The graph parameterization \(L_c\) itself remains valid there.

## 4. The actual endpoint seed and the unchanged closing

Retain the literal cup and the full top rows from S and H:
\[
 p=N\sum_{a=0}^d x^{a-d}|a,d-a\rangle,\quad
 \ell_{\rm o}|a,b\rangle=\frac{x^a}{N}\delta_{a+b,d},
 \quad \ell_{\rm m}|a,b\rangle=\frac{x^b}{N^2}.
 \tag{16}
\]
There is no degree delta in the marked row. Set
\[
 u_0=p^{\otimes k},\quad
 \ell_0=\ell_{\rm o}^{\otimes(k-1)}\otimes\ell_{\rm m},\quad
 y=|0\rangle_2\otimes p^{\otimes(k-1)},\quad
 \xi=\iota_0y .
 \tag{17}
\]
The actual source is invariant, so \(B_cu_0=cu_0\) for every \(c\).
Its explicit seed calibration is
\[
 \boxed{\quad
 u_0=r_c(B_c)\xi=L_cE_dy,\qquad
 E_dy=Nx^{-d}|d\rangle_2\otimes p^{\otimes(k-1)} .
 \quad}
 \tag{18}
\]
To prove the first equality, use C's monic block Krylov basis.
In that basis the kernel of multiplication by \(z-c\), modulo
\(p_N(z)-p_N(c)\), consists exactly of \(r_c(z)\otimes y'\);
this remains true at a multiple root. Its first-head \(d\) component
is \(F_dy'=Ny'\). The same component of the literal cup \(u_0\)
is \(Ny\), fixing \(y'=y\). Equation (12) and \(M_c\iota_0=I\)
give the second expression. Extracting first-head coordinate zero
from the literal cup proves the last formula, with its phase retained.
Also (13) gives \(Q_cu_0=p_N'(c)E_dy\); hence the natural
kernel-to-cokernel comparison kills this nonzero cup at a collision.

For any original unmarked signed braid word \(R\), define
\[
 R_c=\pi_0RL_c,\quad z_0=Nx^{-d}|d\rangle_2
                  \otimes p^{\otimes(k-1)},\quad \ell_c=\ell_0L_c .
 \tag{19}
\]
Since \(R\) commutes with \(B_c\), \(RL_c=L_cR_c\).
Thus the entire original paired-plat scalar, with its prescribed
external factor \(\chi_N\), is exactly
\[
                 \mathcal K_N=\chi_N\ell_cR_cz_0 .
 \tag{20}
\]
This graph reduction is source-faithful even at collisions.
It does not replace \(\ell_c\) by an adjoint row. The saturated
generic source \(\mathcal S_N\) lies inside \(\mathcal E_c\);
the latter, of dimension \(N^{b-1}\), is not identified with
\(\mathcal S_N\) or with the smaller complete invariant multiplicity.
All original crossing factors and Casimir derivative channels remain.
An inserted coupon not commuting with \(B_c\) needs its actual defect.

## 5. Uniform costs and the source-selected projection

For fixed \(b\) and \(|c|\le C_*\), the actual tail satisfies
\(\|T\|\le4(b-1)+C_*\). Recurrence (4) bounds the leading and
trailing continuants by \(C^{a+1}\). Moreover
\[
 |F_a|^{-1}=\frac{|F_{d-a}|}{N}\le\frac{2^{d-a}}N .
 \tag{21}
\]
Consequently all maps in (8), \(D_d,E_d\), and their inverses in
(7) have operator norm at most \(e^{C_{b,C_*}N}\).
There is no \(N\log N\) cost or loss of uniformity at a collision.
The forward representation and the original closing in (19)--(20)
retain these frame costs.

At \(c=2\), S proves \(p_N'(2)\ne0\) for every \(N\ge2\).
Write \(\Pi_2=r_2(B_2)/p_N'(2)\). Since
\(\|p\|=N^{3/2}\), (18) gives the exact source-leg estimate
\[
 \frac{\|r_2(B_2)\xi\|}{\|\xi\|}=N^{3/2},\qquad
              \frac{\|\Pi_2\xi\|}{\|\xi\|}
                         =\frac{N^{3/2}}{|p_N'(2)|}.
 \tag{22}
\]
The coefficient has a sharp subexponential asymptotic:
\[
 \boxed{\quad
 \frac{N^{3/2}}{|p_N'(2)|}
    =2\sqrt\pi\,e^{-\sqrt{\pi N/2}}\bigl(1+O(N^{-1/2})\bigr).
 \quad}
 \tag{23}
\]
Indeed, with \(\theta=\pi/(2N)\), take
\(w=\exp(\operatorname{arsinh}\sqrt{\sin\theta}
       -i\arcsin\sqrt{\sin\theta})\). S gives
\[
 |p_N'(2)|=\frac{N|w^N-w^{-N}|}{2\sqrt{2\sin\theta}} .
 \tag{24}
\]
Here \(N\log|w|=\sqrt{\pi N/2}+O(N^{-1/2})\) and
\(|w^N-w^{-N}|=|w|^N(1+O(e^{-c\sqrt N}))\).
Substitution proves (23). Thus the specified seed-to-cup leg has
no exponential loss at the volume scale, although the global
projector and graph frames need only satisfy exponential bounds.

A quantum correction of the auxiliary parameter makes this coefficient
polynomial while retaining the same principal parabolic generator. Set
\[
 c_N=1+q,\qquad p_N(c_N)=0,\qquad
 \lambda_j=Q^j+qQ^{-j}\quad(0\le j<N).
 \tag{25}
\]
The identity \(p_N(s+q/s)=s^N-s^{-N}\) proves these formulas.
The roots are distinct: a collision for different \(s,t\) with
\(s^N=t^N=1\) would require \(st=q\), which contradicts \(q^N=-1\).
Differentiating that identity at \(s=Q^j\) gives
\[
 p_N'(\lambda_j)=\frac{2NQ^j}{Q^{2j}-q},\qquad
                     p_N'(c_N)=\frac{2N}{1-q}.
 \tag{26}
\]
In particular all these derivative moduli are at least \(N\).
The product formula for the spectral projectors, together with
\(\|B_{c_N}\|\le4b+2\) and \(|\lambda_j|\le2\), bounds them by
\(e^{C_bN}\). The actual seed-to-cup coefficient is now exactly
\[
 \boxed{\quad
 \frac{\|\Pi_{c_N}\xi\|}{\|\xi\|}
 =\frac{N^{3/2}}{|p_N'(c_N)|}
 =\sqrt N\sin\frac{\pi}{2N}
 =\frac{\pi}{2\sqrt N}(1+O(N^{-2})).
 \quad}
 \tag{27}
\]
Here \(\Pi_{c_N}=r_{c_N}(B_{c_N})/p_N'(c_N)\) is asserted over
\(\mathbb C\); an integral projector requires localizing at \(p_N'(c_N)\).
The exact zero-level generator satisfies
\[
 (B_{c_N}-c_NI)-(B_2-2I)
                       =(q-1)(\mathsf K^{-1}-I),\qquad
 \|(B_{c_N}-c_NI)-(B_2-2I)\|\le2|q-1|=O(N^{-1}).
 \tag{28}
\]
The actual source and closing remain precisely (20).
This correction does not calculate a geometric relative framing
period or identify the finite projector with a geometric local cycle.

There is a concrete finite cyclic realization at this corrected parameter.
Define \(C_0(z)=2\), \(C_1(z)=z\), and
\(C_{a+1}(z)=zC_a(z)-qC_{a-1}(z)\). Then
\(C_a(s+q/s)=s^a+q^as^{-a}\), so
\[
 V_N=\frac{B_{c_N}-qC_{N-1}(B_{c_N})}{2},\qquad
 V_N^N=I,\qquad B_{c_N}=V_N+qV_N^{-1},\qquad
                 \Pi_{c_N}=\frac1N\sum_{a=0}^{N-1}V_N^a .
 \tag{29}
\]
Indeed \(V_N\) has eigenvalue \(Q^j\) at \(\lambda_j\).
For the full spectral idempotents \(\Pi_j\), character orthogonality gives
\[
 \frac1N\sum_{a=0}^{N-1}(V_N^a)^*V_N^a
                         =\sum_{j=0}^{N-1}\Pi_j^*\Pi_j .
 \tag{30}
\]
This positive cyclic-average Gram retains all channels and has the
controlled exponential cost above. The operator average in (29) fixes
the actual source; it is not identified with a bounded-time geometric flow.

## 6. Coverage and the remaining source comparison

C already proves the free companion form and controlled Krylov
recurrence; H already gives a smaller exact invariant-source module.
S selects \(c=2\) for the original cup and proves its stable projector
bound. The additional assertions here are the collision-regular
polynomial kernel (12), its free exact sequence over \(\mathcal O_N[c]\),
and the literal seed calibration with coefficients (23) and (27).

The cut and soft-cut texts keep different finite currents and the
actual geometric framing form. The present finite coefficient is
not identified with that form's relative period or with a geometric
local kernel. In particular (20) retains a closing kernel and complex
word phases; no nonzero lower bound for its particular scalar follows.
No geometric cycle, new volume class, or finite-exception theorem
is asserted.

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| C | [Conserved coideal channels](research_conserved_coideal_braid_channels.md) | 437 | b2a8c539742b4662ab8acbf4dc11c9bfa6acd27e895653ccfc47848278899fd4 |
| S | [Source-selected coideal reduction](research_source_selected_coideal_gaussian_reduction.md) | 332 | 6612573f04ffdd0edfae2e40765ffc0fa2babff7426172035388a516a61f061b |
| H | [Complete original invariant multiplicity](actual_complete_source_multiplicity_module.md) | 602 | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| W | [Original cut and relative Ward class](coherent_cut_obstruction_and_ward_relative_class.md) | 336 | 28141e28d4bc08a8acfa4cef9a8549ed7aadb1344f8796617e68282f7b351e4d |
| F | [Literal soft-cut framing density](research_soft_cut_morse_bott_density.md) | 395 | e411f25c7b66b61d865427db1e1f789aeb09b9c76471a303dfdb8d7673fe6f9a |
