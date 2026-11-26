# Polynomially invertible transport of the full radical matching source

The full and low Newton kernels differ by a specified unit on the
tensor product of the original physical algebras. Its forward and
inverse operator norms are polynomial in the level for every fixed
graph. This combines all radical matching terms before estimating
them. Every original first normal, crossing phase and closing row
is retained. The positive norm comparison is not a lower bound for
the resulting scalar observation.

## 1. Original normal coordinates and the inverse physical kernel

Use the complete sources [H] and [C] listed below. Put
\[
 N\ge2,\quad d=N-1,\quad m=\lfloor N/2\rfloor,\quad
 \eta=(-1)^d,\quad q=e^{\pi i/N},\quad
 P_N(z)=2T_N(z/2)+2,\quad \mathcal A_N=\mathbb C[z]/(P_N),
\]
\[
 c_a=2\cos((2a+1)\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{h<j}(c_h-z),\quad
 S_j=\prod_{h=1}^j2\sin(h\pi/N),\quad
 \phi_N(f)=\eta N^2[z^d]\operatorname{rem}_{P_N}f .
 \tag{1}
\]
The double nodes have indices \(0\le a<m\). At odd levels the
additional simple node is \(c_*=-2\). Let \(E_a\) be the full
Hermite idempotent: its value is one at \(c_a\), zero at the other
nodes, and its first derivative is zero at every double node.
At odd levels \(E_*\) is the corresponding simple-node idempotent.
Define
\[
 \delta_a(z)=\frac{\eta P_N(z)}{N^2(z-c_a)}.
 \tag{2}
\]
These are ordinary polynomials interpreted in the full algebra.
The physical residue formula in [H] gives
\[
 \phi_N(f)=\eta\sum_{a<m}\{(4-c_a^2)f'(c_a)-c_af(c_a)\}
                 +\mathbf1_{N\ \mathrm{odd}}f(-2).
 \tag{3}
\]
In particular, using
\(P_N''(c_a)/2=N^2/(4-c_a^2)\), one has
\[
 f=\sum_{a<m}\bigl(f(c_a)E_a+j_a(f)\delta_a\bigr)
            +\mathbf1_{N\ \mathrm{odd}}f(-2)E_*,\qquad
 j_a(f)=\eta(4-c_a^2)f'(c_a),
 \tag{4}
\]
\[
 \delta_a\delta_b=0,\qquad
 f\delta_a=f(c_a)\delta_a,\qquad
 \phi_N(\delta_a)=1,
 \quad \phi_N(E_a)=-\eta c_a.
 \tag{5}
\]
The Chebyshev derivative identity follows by evaluating
\((4-z^2)P_N''-zP_N'+N^2(P_N-2)=0\) at a double root.
Thus (2)--(5) also check their
normalization directly.

Declare the coordinates in (4) orthonormal. This defines the positive
full-jet norm
\[
 \|f\|_{\rm j}^2=\sum_{a<m}(|f(c_a)|^2+|j_a(f)|^2)
                      +\mathbf1_{N\ \mathrm{odd}}|f(-2)|^2.
 \tag{6}
\]
Multiplication by \(\delta_a\) sends its block \((v,n)\) to
\((0,v)\), vanishes on all other blocks, and has norm one.
This is a coordinate norm on the full algebra, not semisimplification.

Set \(L=d-m\) and retain the literal split
\[
 K(z,w)=\sum_{j=0}^d e_j(z)e_j(w)=K_<(z,w)+H(z,w),\qquad
 K_<=\sum_{j=0}^{L}e_j\otimes e_j,\quad
 H=\sum_{r=0}^{m-1}e_{d-r}\otimes e_{d-r}.
 \tag{7}
\]
Source [H] proves
\[
 e_{d-r}=\sum_{a=0}^r b_{ra}\delta_a,\qquad
 b_{ra}=(-1)^{r+a}\frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}},
 \quad |b_{ra}|\le2,\quad s_h=2\sin(h\pi/N).
 \tag{8}
\]
Indeed its original trace against every \(f\) is
\(\sum_a b_{ra}f(c_a)\); nondegeneracy of the original Frobenius
pairing gives (8). At \(N=2\), \(e_1=\delta_0=-z/4\) and
\(b_{00}=1\), so the same statements hold directly.

On the double-node grid define
\[
 E_{ar}=e_r(c_a),\quad B=(b_{ra}),\quad
 G_{ab}=K(c_a,c_b),\quad W=B^{\mathsf T}B
                  \qquad(0\le a,r,b<m).
 \tag{9}
\]
Newton interpolation at these distinct nodes gives \(B=E^{-1}\).
Since \(e_j(c_a)=0\) for \(j>a\),
\[
 \boxed{\quad G=EE^{\mathsf T},\qquad W=G^{-1},\qquad
 H=\sum_{a,b<m}W_{ab}\delta_a\otimes\delta_b.\quad}
 \tag{10}
\]
Both matrices are real positive definite. Also
\(G_{ab}\ge1\), because all its nonzero Newton summands are
positive, and \(|W_{ab}|\le4m\) by (8). No polynomial bound for
the condition number of \(G\) is asserted; [H] proves exponential
ill-conditioning of \(W\).

## 2. The exact whole-matching unit and its polynomial inverse

Let \(I\) be a fixed finite set of vertices actually subjected to
the original traces. Choose a finite collection \(\mathcal E\)
of original same-index edges \(K\), each with two distinct endpoints
in \(I\). Other kernels, coupons and all ordinary free-boundary
variables are left in an arbitrary attachment \(A\).
Parallel chosen edges are allowed and remain distinct edge occurrences.
Only the variables in \(I\) are reduced modulo \(P_N\).

For a chosen edge \(e=vw\), put
\[
 J_{ab}=\frac{W_{ab}}{G_{ab}},\qquad
 V_e=\sum_{a,b<m}J_{ab}\delta_a^{(v)}\delta_b^{(w)}
          \ \in\ \mathcal A_N^{\otimes I}.
 \tag{11}
\]
The quotient here is entrywise, not matrix multiplication. Equations
(5),(10), and \(K_<(c_a,c_b)=G_{ab}\) give exactly
\[
 K_e=K_{<,e}(1+V_e),\qquad
 V_e^2=0,\qquad V_eV_f=0\quad(e,f\text{ share a vertex}).
 \tag{12}
\]
Multiplication by \(\delta_a\delta_b\) sees only the value of
\(K_<\); its mixed normal is precisely \(W_{ab}\). No derivative
of \(K_<\) is discarded in (12).

Let \(\mathfrak M\) be all matchings of the chosen multigraph,
including the empty one, and let \(\nu\) be its matching number.
Then the following element and inverse are explicit:
\[
 \boxed{\quad
 U=\prod_{e\in\mathcal E}(1+V_e)
       =\sum_{M\in\mathfrak M}\prod_{e\in M}V_e,
 \qquad
 U^{-1}=\sum_{M\in\mathfrak M}(-1)^{|M|}\prod_{e\in M}V_e.
 \quad}
 \tag{13}
\]
All factors commute. Each inverse factor is \(1-V_e\), and
overlapping products vanish by (12), proving both formulas.
Equivalently \(U=\exp(\sum_eV_e)\), with a terminating exponential.

Equip \(\mathcal A_N^{\otimes I}\) with the tensor norm from (6).
Different physical color assignments are orthogonal. On one such
assignment, multiplication by \(V_e\) is either zero or the
rank-one map on its two normal slots with coefficient \(J_{ab}\).
It is tensored with the identity on other slots. Consequently
\[
 \|M_{V_e}\|=\max_{a,b}|J_{ab}|\le4m,\qquad
 \boxed{\quad
 \|M_U\|,\ \|M_{U^{-1}}\|
       \le P_{\mathcal E}(4m):=
              \sum_{M\in\mathfrak M}(4m)^{|M|}
       =O_{\mathcal E}(N^\nu).\quad}
 \tag{14}
\]
Here \(M_f\) means multiplication by the indicated algebra element.
The triangle inequality and submultiplicativity prove (14).

For arbitrary signed powers and any level-dependent actual attachment,
set
\[
 F_< = A\prod_{v\in I}R(z_v)^{n_v}
                       \prod_{e\in\mathcal E}K_{<,e},\qquad
 F=A\prod_{v\in I}R(z_v)^{n_v}\prod_{e\in\mathcal E}K_e.
\]
Then
\[
 F=UF_<,\qquad
 P_{\mathcal E}(4m)^{-1}\|F_<\|_{\rm j}
 \le\|F\|_{\rm j}\le P_{\mathcal E}(4m)\|F_<\|_{\rm j}.
 \tag{15}
\]
These are exact source identities coefficientwise in every ordinary
free variable and all its derivatives. They also hold with any
independent exterior Hilbert space tensored onto the norm. A selected
loop has \(H(z,z)=0\) in the original algebra, so it may simply be
left untouched or assigned \(V_e=0\).

The statement applies to the chosen actual \(K_T\) connections.
An identity connection \(K_I\), or a free ordinary-variable factor,
has not silently been replaced by \(K_T\) or reduced to these jets.

## 3. Original closing, including its complete monomer--dimer row

Write \(\ell=\bigotimes_{v\in I}\phi_N\). The closed source is
\[
                         \ell(F)=(\ell M_U)(F_<).
 \tag{16}
\]
Thus the actual observation is transported to \(\ell M_U\), not
replaced by \(\ell\). Its norm is at most
\((5m+1)^{|I|/2}P_{\mathcal E}(4m)\), by (3),(6),(14).
Any further prescribed exterior covector remains unchanged.

An explicit row formula keeps every original normal. Put
\(F_0=A\prod_eK_{<,e}\), and fix a physical assignment
\(\mathbf c\) at the selected vertices. Let \(D(\mathbf c)\)
be the vertices assigned double nodes. For \(S\subseteq D(\mathbf c)\),
write \((F_0)_S(\mathbf c)\) for its mixed normal coordinate,
obtained by applying \(\prod_{v\in S}\eta(4-c_v^2)\partial_{z_v}\).
Retain
\[
 r_v=R(c_v)^{n_v},\qquad
 t_v=-\eta c_v+\eta(4-c_v^2)n_v\frac{R'(c_v)}{R(c_v)}
     =-\eta c_v+i\eta n_v(d-2a_v)
                       \sin((2a_v+1)\pi/N)
 \tag{17}
\]
at double nodes. Formula [C](21) gives the last equality. The actual
values are \(R(c_a)=\kappa(-1)^aq^{a(a+1)}\),
\(\kappa=q^{d^2/2}\), including the odd simple value, so all \(r_v\)
have modulus one.

The contribution of \(\mathbf c\) to the original closing is exactly
\[
 \boxed{\quad
 \left(\prod_vr_v\right)
 \sum_{S\subseteq D(\mathbf c)}(F_0)_S(\mathbf c)
 \sum_{M\in\mathfrak M(\mathcal E[D(\mathbf c)\setminus S])}
       \left(\prod_{vw\in M}J_{a_va_w}\right)
       \prod_{v\in D(\mathbf c)\setminus(S\cup V(M))}t_v .\quad}
 \tag{18}
\]
Sum (18) over all physical assignments. Odd simple slots supply their
value row one and never acquire an extra normal. To prove (18), expand
\(F_0\) in the basis (4). A matching normal annihilates an already
occupied normal slot. On an unoccupied double slot the original row
\(\phi_N(R^{n_v}\cdot)\) is \(r_v(t_v,1)\); on a simple slot it
is \(r_v\). This proves the formula by the finite product rule.
It allows an arbitrary joint attachment, without factorization.

## 4. Metric covariance and the remaining observation

Let \(\mathbf1\) be the constant double-node vector and \(e_0\) its
first coordinate vector. Equations (8)--(10) imply
\[
 G e_0=\mathbf1,\quad W\mathbf1=e_0,\qquad
 G D_nW\mathbf1=R(c_0)^n\mathbf1,\quad
 \mathbf1^{\mathsf T}W D_nG=R(c_0)^n\mathbf1^{\mathsf T},
 \tag{19}
\]
where \(D_n=\operatorname{diag}R(c_a)^n\). At zero power,
\(GD_0W=WD_0G=I\), so unweighted inverse-kernel connections cancel
exactly. With a nonzero power the diagonal remains in its actual slot.
In low Newton coordinates \(B D_nE\) is unitary for the positive
metric \(E^{\mathsf T}E\); that metric is not asserted polynomially
comparable to the coefficient metric of a matching contraction.

For one radical edge the original bilinear contraction is
\(f^{\mathsf T}D_nWD_pg\). It is a positive Gram when
\(g=\overline f\) and \(p=-n\), because \(W=B^{\mathsf T}B>0\).
The general original attachment has no such reflected pairing.
Likewise the monomers (17) do not have a common positive real part.
Indeed multiplication by \(R^n\) on a double-node jet is
\(R(c_a)^n\left(\begin{smallmatrix}1&0\\
i\eta n(d-2a)\sin((2a+1)\pi/N)&1\end{smallmatrix}\right)\).
Hence \(\|M_{R^{\pm n}}\|\le1+|n|N\): fixed powers do not change
the exponential rate of the full raw tensor norm, although their
original scalar observations can change.
Equations (14)--(15) preserve the exponential rate of a nonzero full
tensor-jet norm. They give neither positivity nor a lower bound for
(16) or (18), and no selected geometric-cycle coefficient.

Only selected variables have been quotiented. Subsequent turns do not
preserve the radical: \(T\delta_0=T e_d=1\). Thus this exact fixed-network
transport is not a semisimple tangle functor or a license to discard
normal data before further original operations.

## 5. Direct sources

* [H: Full high-Newton radical contraction](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
* [C: Original arbitrary-power source compilation](research_arbitrary_power_source_compilation.md),
  SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f.

The endpoint-current boundary-unit theorem concerns a different,
already-contracted Ward-current polynomial. It does not supply the
kernel factorization (12) or the whole tensor transport (13)--(18).
