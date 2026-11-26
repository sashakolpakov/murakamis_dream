# The original marked cap becomes a corner in coherent coordinates

24 November 2026. Written research proof.

The original transformed closing restricts to one physical corner in the
coherent coordinates used to bound the shared boundary resolvent.
The ordinary caps remain literal.
Its intrinsic dual norm is bounded above and below by explicit powers
of the level. No new closing functional is chosen.

There is a further source-faithful reduction. The central integer-degree
projection of the coherent packet retains the entire invariant tensor
at every width. The original input and closing in this smaller packet
have exact polynomial norm product. Earlier complete source modules
already have central-degree coordinates; the new statements identify
this particular orthogonal projection and this coherent marked row.
They do not bound the remaining coherent word or prove its volume rate.

## 1. Actual source and coherent coordinates

Use the complete physical conventions of [T,O,M,P,D]:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1}=q^d,\quad \theta=\pi/(2N),\quad \xi=q^{-3}.
 \tag{1}
\]
On the original orthonormal head \(V=\mathbb C^N\),
\[
 E|a\rangle=(Q^{-a}-1)|a-1\rangle,\quad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\quad
 K|a\rangle=xQ^{-a}|a\rangle .
 \tag{2}
\]
Missing arrows vanish. The unrolled weight is
\(H|a\rangle=(d-2a)|a\rangle\), and the coproducts are
\[
 E_{12}=E_1K_2+E_2,\qquad
 F_{12}=F_1+K_1^{-1}F_2,\qquad K_{12}=K_1K_2.
 \tag{3}
\]
All norms below are unnormalized physical Euclidean norms or their
induced dual norms.
The actual pair Casimir is
\(\Omega=F_{12}E_{12}+qK_{12}+q^{-1}K_{12}^{-1}\).

Let \(b=2k\ge4\), \(W=V^{\otimes(b-2)}\), and let
\(\mathcal I_b\) be the full root invariant space with unrolled
weight zero. Let \(\mathcal S_b\subset\mathcal I_b\) be the actual
saturated specialization of generic invariant tensors. The original
turns are
\[
 p_{ab}=Nx^{-b}\delta_{a+b,d},\qquad
 \ell_{ab}=x^a\delta_{a+b,d}/N,\qquad m_{ab}=x^b/N^2.
 \tag{4}
\]
The marked row has no degree delta. The literal snakes hold,
\(mp=1\), \(\ell p=0\), and
\(\|p\|=N^{3/2}\), \(\|\ell\|=N^{-1/2}\).

Write
\[
 \eta_a=\frac{1-q^3}{2}q^{3a},\qquad
 \zeta_a=\frac{1-q^{-3}}2x^a,\qquad
 \mathscr D_b=\eta\otimes I_W\otimes\zeta .
 \tag{5}
\]
By [O], this observation is faithful on \(\mathcal I_b\) and on
\(\mathcal S_b\). Its inverse retains the unrolled and regular
divided-current source equations. Put
\(\mathcal Y_b=\mathscr D_b(\mathcal S_b)\).

For a nilpotent argument \(t^N=0\), set
\[
 \mathsf e_N(t)=\sum_{r=0}^{d}\frac{t^r}{(Q;Q)_r},\qquad
 S_W=\mathsf e_N(E_WK_W^{-1}/\xi)^{-1}.
 \tag{6}
\]
The finite inverse exists, with the opposite Euler coefficients, as
proved in [T]. This is the coherent change that makes
\(E_W-\xi K_W\) unitary and bounds the normalized shared resolvent
by three. The transformed actual source and its original row are
\[
 \overline{\mathcal Y}_b=S_W^{-1}\mathcal Y_b,\qquad
 \overline\Lambda_b(w)=\Lambda_b(S_Ww),\qquad
 \Lambda_b(y)=(\ell^{\otimes(k-1)}\otimes m)\Phi_{f_y}.
 \tag{7}
\]
Here \(\Phi_{f_y}\) is the literal source reconstruction, not an
independently prepared exterior. The original external factor
\(\chi_N\), when present, multiplies this row unchanged.

## 2. The source slice that selects the corner

Let \(A=V\otimes V\). Literal currying identifies invariant tensors
with the actual unrolled Hopf maps \(f:A\to W\):
\[
 \Phi_f=(I\otimes f\otimes I)(p_{12}\otimes p_{34}),\qquad
 \mathscr D_b\Phi_f=f(\mathbf u),
 \tag{8}
\]
\[
 \mathbf u_{ab}=C_D\tau^a,\qquad
 \tau=-Q^{-1},\qquad C_D=N^2\sin^2(3\theta)q^{3d}.
 \tag{9}
\]
All these scalars are those of [O,T]. In particular they are nonzero
at every \(N\ge2\). Let \(P_t^A\) denote the orthogonal projection
onto pair integer degree \(a+b=t\), and define
\[
 c_{\rm edge}=\frac{2C_D\tau^d}{1-q^3}.
 \tag{10}
\]
The essential source identity is
\[
 \boxed{\qquad P_d^A S_A^{-1}\mathbf u
                      =c_{\rm edge}|d,0\rangle .\qquad}
 \tag{11}
\]

We prove it with the finite root cutoff retained. On the pair put
\[
 A_1=E_1K_1^{-1},\qquad A_2=K_1^{-1}E_2K_2^{-1}.
\]
Then \(E_AK_A^{-1}=A_1+A_2\) and \(A_1A_2=QA_2A_1\).
The root Gaussian expansion gives
\[
 S_A^{-1}=\sum_{i+j<N}
       \frac{\xi^{-(i+j)}A_2^jA_1^i}{(Q;Q)_i(Q;Q)_j}.
 \tag{12}
\]
The product \(\mathsf e_N(A_2/\xi)\mathsf e_N(A_1/\xi)\)
has the same terms with \(i+j<N\), plus terms with \(i+j\ge N\).
Each latter term lowers total physical degree by at least \(N\).
It cannot contribute to output degree \(d\), since the required
input degree is at least \(d+N=2d+1\), beyond the actual pair.
Consequently
\[
 P_d^A S_A^{-1}
   =P_d^A\mathsf e_N(A_2/\xi)\mathsf e_N(A_1/\xi).
 \tag{13}
\]
This is a slice identity only. The two finite Euler factors have
not been asserted to factor the whole operator in (6).

On the first-head factor \((\tau^a)_a\), direct use of (2) gives
\[
 \frac{\mathsf e_N(A_1/\xi)(\tau^a)_a}{\tau^a}
   =\sum_{i=0}^{d-a}Q^i{a+i\brack i}_Q
   ={N\brack a+1}_Q=\delta_{a,d}.
 \tag{14}
\]
The finite sum follows by telescoping the Gaussian Pascal identity.
For \(a<d\), its top index is \(N\), its lower index lies strictly
between zero and \(N\), and its root value is zero. For \(a=d\)
the sum has its single value one, as does \({N\brack N}_Q\).
Thus the first factor collapses the first head to \(d\), including
all endpoints.

At that head, \(K_1^{-1}\) has eigenvalue \(x\).
On the second-head all-ones vector the value at output zero of the
remaining Euler factor is
\[
 \sum_{j=0}^{d}\xi^{-j}
       =(q^3Q;Q)_d=\frac{2}{1-q^3}.
 \tag{15}
\]
For the first equality, \((xE_2K_2^{-1})^j\mathbf1\) at zero
has coefficient \((Q;Q)_j\). The geometric sum uses \(\xi^N=-1\).
The product equality also follows from
\((q^3Q;Q)_N=2\) by removing its last factor \(1-q^3\).
Equations (13)--(15) prove (11), with its exact phase and factor two.
No small-level exception is needed, including \(N=2\).

## 3. The original closing on the coherent source

At four heads the actual curried map is an endomorphism of \(A\).
By [P] it is a unique polynomial \(g(\Omega)\) modulo the complete
Casimir polynomial, with every repeated-root derivative retained.
Let \(J=\Omega|_{A_d}\) in the original degree-\(d\) basis
\(|a,d-a\rangle\). The literal closing functional satisfies
\[
 \lambda_4(g)=\phi(g)=(g(J))_{0,d}.
 \tag{16}
\]
This is the fixed-root marked functional of [P,T], not an ordinary
trace on the distinct Casimir values.

The Casimir commutes with the total \(E,K\), and therefore with
\(S_A\). It also preserves full integer degree. If
\(w=S_A^{-1}g(\Omega)\mathbf u\), (11) implies
\[
 w_{0,d}=c_{\rm edge}(g(J))_{0,d}.
\]
Thus the original transformed row is exactly
\[
 \boxed{\qquad \overline\Lambda_4(w)
                  =c_{\rm edge}^{-1}w_{0,d}
                  \quad(w\in\overline{\mathcal Y}_4).\qquad}
 \tag{17}
\]
Equation (17) gives another physical extension of the same restricted
functional as \(\alpha_4S_A\) from [T]. The intrinsic dual estimate
below uses the new corner row.

For \(b=2k\), let
\[
 L_{\rm int}=I\otimes\ell^{\otimes(k-2)}\otimes I:W\to A.
 \tag{18}
\]
These are exactly the interior ordinary caps in the original last-mark
closing. They are actual Hopf maps and intertwine the finite Euler
operators, so \(L_{\rm int}S_W=S_A L_{\rm int}\).
For every source map \(f\), the map \(L_{\rm int}f:A\to A\)
is an actual pair endomorphism. Apply (17) to it. The full-width
original row therefore has the exact extension
\[
 \boxed{\qquad
 \overline\Lambda_b(w)
    =c_{\rm edge}^{-1}\langle0,d|L_{\rm int}w,
                       \quad w\in\overline{\mathcal Y}_b .
 \qquad}                                                       \tag{19}
\]
No marked-cap relocation is used. All original powers of \(N\), the
last mark and the external \(\chi_N\) remain on this formula.

## 4. Polynomial intrinsic dual norm on the actual saturated source

Let \(\|\overline\Lambda_b\|_{\overline{\mathcal Y}_b^*}\)
mean the dual norm with the physical norm restricted to this transformed
source. From (10), \(|C_D|=N^2\sin^2(3\theta)\), and (19),
\[
 \|c_{\rm edge}^{-1}\langle0,d|L_{\rm int}\|
       =\frac{N^{-(k+2)/2}}{\sin3\theta}.
 \tag{20}
\]
This is an extension norm, hence an upper bound for that intrinsic norm.

There is also a source witness with no unknown scalar in its definition.
Prepend cups by the actual intertwiner
\[
 J_{\rm chain}(v\otimes w)=p^{\otimes(k-2)}\otimes v\otimes w.
 \tag{21}
\]
The caps (18) run through the seams of this chain. Repeated literal
snake equations give \(L_{\rm int}J_{\rm chain}=I_A\).
This differs from inserting cups between the two free heads, which
would produce zero ordinary bubbles under (18).

Set \(f_*=J_{\rm chain}(p\ell)\). Its curried tensor is a regular
generic cup matching and therefore belongs to \(\mathcal S_b\).
The original closing has value \(\phi(p\ell)=1\).
Since \(S_A^{-1}p=p\), its transformed observation is
\[
 w_*=S_W^{-1}f_*(\mathbf u)
          =J_{\rm chain}p\,\ell(\mathbf u),\qquad
 \ell(\mathbf u)=\frac{2C_D}{N(1-\xi)}.
 \tag{22}
\]
For the last identity use \(x\tau=\xi\) in the literal cap (4).
The norm of \(J_{\rm chain}p\) is \(N^{3(k-1)/2}\).
Using this actual source vector in the dual norm gives
\[
 \boxed{\qquad
 \frac{N^{-(3k-1)/2}}{\sin3\theta}
 \ \le\ \|\overline\Lambda_b\|_{\overline{\mathcal Y}_b^*}
 \ \le\ \frac{N^{-(k+2)/2}}{\sin3\theta}.
 \qquad}                                                       \tag{23}
\]
These inequalities hold at every \(N\ge2\). In particular the
intrinsic co-source norm has zero exponential rate at fixed width.
If \(\chi_N\) is folded into the row, both bounds are multiplied
by \(|\chi_N|\); no bound on that separate original factor is implied.
This is a norm of a functional, not a nonzero lower bound for its value
on an arbitrary word state.

## 5. A faithful orthogonal degree projection

Put \(D=(k-1)d\), and let \(P_D^W\) be the physical orthogonal
projection onto middle integer degree \(D\); write \(W_D=\operatorname{ran}P_D^W\).
An unrolled map
\(f:A\to W\) sends input degree \(t\) to degree
\((k-2)d+t\). Therefore (8),(11) give
\[
 \boxed{\qquad
 \mathscr F_b\Phi_f:=P_D^W S_W^{-1}\mathscr D_b\Phi_f
                         =c_{\rm edge} f(|d,0\rangle).
 \qquad}                                                       \tag{24}
\]
In the literal curry coordinates this is also
\[
 f(|d,0\rangle)=\frac{x^{2d}}{N^2}\Phi_{0,W,d}.
 \tag{25}
\]
The unsimplified scalar records the ordered cup normalization; \(x^{2d}=Q\).

Evaluation at \(|d,0\rangle\) is faithful on all these intertwiners.
Indeed [P]'s middle Casimir \(J\) is tridiagonal with every adjacent
entry nonzero. The vectors \(J^r|d,0\rangle\), \(0\le r<N\),
form a triangular basis of \(A_d\). The actual \(E,F\) surjections
in [P] generate the whole pair from \(A_d\). Hence an intertwiner
vanishing at \(|d,0\rangle\) vanishes everywhere. This argument
retains the entire pair, including each Casimir Jordan direction.

The complete dimension formula in [M] is
\[
 \dim\mathcal I_b=[z^{(k-1)d}](1+z+\cdots+z^d)^{2k-2}
                          =\dim W_D .
 \tag{26}
\]
It follows that (24) is an isomorphism \(\mathcal I_b\to W_D\).
The saturated image is the same explicit physical source kernel
already identified in [D]:
\[
 \mathscr F_b(\mathcal S_b)
      =\ker(\mathcal J_E^W:W_D\longrightarrow W_{D-N}),\qquad
 \mathcal J_E^W=
 \left[\frac{E_W(\zeta)^N}{1-\zeta^{2N}}\right]_{\zeta=q}.
 \tag{26a}
\]
The target is zero if its degree is negative. To prove inclusion,
take a regular generic invariant lift and its literal generic curry
\(f_\zeta\). Since the input \(|d,0\rangle\) has degree \(d<N\),
\(E_A(\zeta)^N|d,0\rangle=0\) identically. Thus
\(E_W(\zeta)^N f_\zeta|d,0\rangle=0\).
Division by the specified factor and specialization give the equation
in (26a). The nonzero scalar \(c_{\rm edge}\) does not change its
kernel. The dimension and surjectivity theorem in [D] gives
\(\dim\mathcal S_b=\dim W_D-\dim W_{D-N}\), equal to that kernel's
dimension, proving equality. Its redundant \(\mathcal J_F\) equation
and differentiated inhomogeneous source equations retain [D]'s scope.
In particular, the saturated source is not every vector of \(W_D\)
when this divided-current condition is nontrivial.

The prescribed input and row in these degree coordinates are especially
simple:
\[
 z_{\rm in}=c_{\rm edge}|d\rangle\otimes
                  p^{\otimes(k-2)}\otimes|0\rangle,
 \qquad
 \lambda_D=c_{\rm edge}^{-1}\langle0,d|L_{\rm int}.
 \tag{27}
\]
The row is already supported in degree \(D\). Its restriction to
\(W_D\) has the same norm as the displayed physical extension.
Consequently the exact polynomial boundary product is
\[
                        \|z_{\rm in}\|\,\|\lambda_D\|
                                      =N^{k-2}.
 \tag{28}
\]
The exponential input cost of the full coherent packet in [T] is thus
absent from this source-faithful projected input. This does not make
the transported word norm inexpensive.

For each original regular signed braid the correct reduced operator
is \(\mathscr F_b R_i\mathscr F_b^{-1}\), restricted to (26a) when
required. Products and the literal closing transport exactly. One cannot
instead insert \(P_D^W\) between untransported crossings: the projection
need not commute with those operators or reconstruct their components.

## 6. Actual generators on the projected packet

The projected Casimirs also have direct formulas. Write \(n=b-2\),
and let totals over the indicated proper blocks use (3). On \(W_D\),
put
\[
 \begin{split}
 L&=q^{-1}F_1K_1E_{2,\ldots,n}-K_1-K_1^{-1},\\
 R&=qK_n^{-1}E_nF_{1,\ldots,n-1}-K_n-K_n^{-1}.
 \end{split}
 \tag{29}
\]
Then the first and last original pair Casimirs transport to \(L,R\),
and every interior one remains \(\Omega^W_{i-1,i}\).
These operators preserve integer degree. Their full physical bounds are
\[
                         \|L\|,\|R\|\le4(n-1)+2.
 \tag{30}
\]
These are bounds for the Casimirs, not for their level-dependent braid
polynomials.

Here is an endpoint derivation fixing the orders. Let
\(z=f|d,0\rangle\); the common scalar in (24) is irrelevant to operator
conjugation. The literal total actions on this input give
\[
 f|d-1,0\rangle=\frac{E_Wz}{x(Q-1)},\qquad
 f|d,1\rangle=\frac{F_Wz}{x(1-Q)}.
 \tag{31}
\]
The denominators are nonzero, and will cancel. Apply [T]'s two cup
transpose operator identities before evaluating on this input.
At the left endpoint the first input-head \(F\) term is zero,
since \(F|d\rangle=0\). The resulting Casimir is
\[
 q^{-1}F_1K_1E_Wz+(Q-1)K_1z+2qz.
 \tag{32}
\]
On degree \(D\), the total \(K_W\) is one. In
\(E_W=E_1K_{2,\ldots,n}+E_{2,\ldots,n}\), its first term
therefore contributes \(qF_1E_1z\) to (32).
The one-head identity \(FE=-2-qK-q^{-1}K^{-1}\) cancels the
remaining diagonal terms, giving \(Lz\).

The right cup transpose similarly gives
\[
 qK_n^{-1}E_nF_Wz+(Q-1)K_n^{-1}z+2qz.
 \tag{33}
\]
Use \(F_W=F_{1,\ldots,n-1}+K_{1,\ldots,n-1}^{-1}F_n\)
and \(K_Wz=z\). The second term contributes \(qE_nF_nz\).
The identity \(EF=-2-q^{-1}K-qK^{-1}\) now gives \(Rz\).
This proves both formulas, including the physical endpoint zeros.
The interior formulas follow by disjoint contraction.
The bounds (30) use \(\|E_{2,\ldots,n}\|,\|F_{1,\ldots,n-1}\|
\le2(n-1)\), and the local head bounds in (2).

Put \(\kappa=q^{d^2/2}\). For the original degree-\(<N\) Hermite
braid polynomial \(r_N\),
the reduced positive crossings are \(\kappa r_N(L)\),
\(\kappa r_N(R)\), and \(\kappa r_N(\Omega^W_{i-1,i})\).
Their negatives use the literal inverse polynomial modulo the complete
Casimir polynomial. All first derivatives at repeated roots remain.
These matrices preserve (26a) and satisfy the original braid relations
because they are exact transports. No sharp coherent product bound
or bounded degree for \(r_N\) is inferred from (30).

## 7. Scope and earlier complete reductions

[M] already gives complete all-width central-degree source modules,
bounded-degree Casimir formulas and polynomial original boundaries.
At four heads, the coordinate \(f|d,0\rangle\) is exactly
\((x^d/N)Jw\) in its opposite highest chart, where \(w,J\) are
[M]'s original multiplicity vector and recoupling matrix.
[O] already proves faithful observations
with explicit reconstruction and actual source constraints. [P] already
retains every repeated-root Casimir normal and gives the original
endpoint functional. [T] already gives the coherent metric, its full
input cost and the literal physical closing row. [D] already proves
the regular divided-current kernel and its exact source dimension.

The additions are the exact source slice (11), the resulting cheap
extension of the original coherent closing, the actual-source dual
sandwich (23), and the identification of the faithful orthogonal degree
projection (24), with the actual generators on that projected packet.
The finite Euler tools, the existence of central multiplicity coordinates
and the earlier source kernel are not claimed new.

All statements concern the actual fixed-root source. Differentiated
source families keep their original inhomogeneous normal equations.
No geometric saddle, arbitrary coherent scalar noncancellation, or
finite-exception volume theorem after general short partial fillings
follows from the polynomial boundary budget alone.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| T | [Boundary Casimir transport](research_all_width_marked_boundary_casimir_transport.md) | 828 | 357eee1e3cd0e65149a77fb2fb714bdd75c3a5e64642ac1f26bb3c08daadf381 |
| O | [All-width marked-mode observation](research_all_width_marked_mode_observation.md) | 591 | b2ec8912696338d23e67e2ceb3e69a3fd5a1e20dfcfbe49228cd514a7d40f3f7 |
| M | [Complete original source multiplicities](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_source_multiplicity_module.md) | 602 | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| P | [Full physical pair commutant](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_pair_casimir_commutant_and_rotated_trace.md) | 331 | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| D | [All-width divided-current source restriction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_all_width_divided_source_projection.md) | 204 | dc83b5e232a3d258f516a479d7257e85b9e5663a38e166f07c6ad9ae81004a68 |

Only written mathematics, source reads and text/hash operations were used.
Earlier final notes, the ledger and public manuscripts are unchanged.
