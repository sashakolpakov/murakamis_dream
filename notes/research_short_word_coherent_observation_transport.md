# Sublinear polynomial observations through fixed Conway words

Written research proof, 22 November 2026.

For any fixed word of original signed crossings and turns, polynomial
observations of sublinear Casimir degree retain the exponential norm
rate of the transported coherent packet. Both the packet and the
observation are transported. The input bidisc has a positive radius
depending on the word, and the comparison is in the original
Newton coefficient norm.

The proof combines an exact generating-unit gauge identity with
explicit finite-head extraction operators. No bound for the norm or
condition number of the word is used. The transported packet can
have a different rate from the untransported one. Its new rate and
its original scalar closing are not evaluated here.

## 1. Original operations and the joint observation family

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 s_j=2\sin(\pi j/N),\quad S_j=\prod_{r=1}^j s_r,\quad S_0=1,
\]
\[
 c_j=qQ^j+q^{-1}Q^{-j},\quad c_0=q+q^{-1},\quad
 P_N(\zeta)=2T_N(\zeta/2)+2,\quad
 \mathcal H_N=\mathbb C[\zeta]/(P_N).
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind.
Give the original Newton basis
\[
 e_j(\zeta)=S_j^{-2}\prod_{r<j}(c_r-\zeta),\qquad 0\le j<N,
\]
its coefficient Euclidean norm. This retains the entire Hermite
algebra, including its first spectral normals. It is not the
uniform physical Hilbert--Schmidt metric.

Let \(Z\) be multiplication by \(\zeta\), let \(J\) be the
genuine turn, and write \(L=JZJ\). Their exact actions are
\[
 Ze_j=c_je_j-s_{j+1}^2e_{j+1},\quad
 Je_j=e_{d-j},\quad
 Le_j=c_je_j-s_j^2e_{j-1},\qquad
                         \|Z\|,\|L\|\le6 .
 \tag{2}
\]
Missing end vectors are zero. The positive crossing is the original
unit \(R\), with \(\kappa=q^{d^2/2}\), not a new phase surrogate.
For each integer \(n\), put
\[
                         L_n=R^{-n}LR^n.
 \tag{3}
\]
A fixed word \(W\) means a fixed finite product of \(J\)'s and
integer powers of multiplication by \(R\). Its original scalar
carriers remain included.

Use the centered generating unit of the full-tensor theorem:
\[
 A_N(t,\zeta)=\sum_{a=0}^d p_a(\zeta)t^a,\qquad
 f_a=N^{-1/2}R\,p_a,\qquad
 \mathcal F_N(t)=N^{-1/2}R\,A_N(t,\zeta).
 \tag{4}
\]
Define the actual product packet
\[
 w_N(y,z)=\mathcal F_N(y)\mathcal F_N(z)
             =N^{-1}R^2A_N(y,\zeta)A_N(z,\zeta).
 \tag{5}
\]
It is a unit of the algebra when \(|y|,|z|<1\). Indeed the
physical node products of \(A_N\) have all their zeros on
\(|t|=1\), and nonzero values imply invertibility in each full
local Artin factor. A common normalization of the two inputs
does not change any ratio below.

For a polynomial \(P\), the joint family is \(WP(Z)w_N\).
It is not \(P(Z)Ww_N\).
Write \(\|P\|_2\) for its ordinary monomial coefficient norm.

## 2. Uniformly bounded transported trace operators

We first record explicitly the operator bounds needed below.
The exact Newton matrix of \(L_1\) has entries
\[
 (L_1)_{jj}=4qQ^j-q(1+Q)Q^{2j},\qquad
 (L_1)_{j-1,j}=(L_1)_{j,j-1}=-(1-Q^j)^2.
 \tag{6}
\]
This is the full finite-band conjugation identity, including \(N=2\);
it is obtained by conjugating its displayed tridiagonal matrix by
the unitary \(J\). Thus \(\|L_1\|\le14\).
There is also the divisor-free operator recurrence
\[
                 L_{n+1}+qZL_n+q^2L_{n-1}=8qI
                               \qquad(n\in\mathbb Z).
 \tag{7}
\]
Starting from \(L_0=L,L_1\), this bounds every fixed \(L_n\)
uniformly in \(N\), in both directions.

The exact conjugation identities are
\[
 JZJ=L,\quad JLJ=Z,\quad JL_1J=L_{-1},\qquad
 R^{-m}ZR^m=Z,\quad R^{-m}L_nR^m=L_{n+m}.
 \tag{8}
\]
All scalars in the original braid relation cancel in these
conjugations. Equation (7) expresses each \(L_n\) as a
noncommutative polynomial in \(Z,L,L_1\), with Laurent-polynomial
coefficients in \(q\). Substitution in (8) therefore proves, for
every fixed word and integer \(n\),
\[
       \|WZW^{-1}\|\le C_W,\qquad
                    \|WL_nW^{-1}\|\le C_{W,n},
 \tag{9}
\]
with constants independent of \(N\).
The statement bounds these specified observables; it bounds neither
\(W\) nor \(W^{-1}\). No positive adjoint relation for \(R\)
is asserted.

## 3. Exact conjugation by a generating unit

Let \(M_t\) be multiplication by \(A_N(t,\zeta)\), and put
\(b_t(\zeta)=1+t\zeta+t^2\).
For every \(|t|<1\) and integer \(n\), the exact full-algebra
identity is
\[
 \boxed{\quad
 b_t(Z)M_tL_nM_t^{-1}
       =L_n-c_0tL_{n+1}+t^2L_{n+2}+8tI .
 \quad}
 \tag{10}
\]
We prove this with its original first normals and endpoint terms.

Write \(\zeta(v)=v+v^{-1}\), and use the original rational
difference coefficients
\[
 a(v)=-\frac{(qv-1)^3}{q(v^2-1)(qv+1)},\qquad
 \bar a(v)=a(v^{-1}),\qquad
 c_0+a(v)+\bar a(v)=\frac8{c_0+\zeta(v)}.
 \tag{11}
\]
The bar over \(a\) in this display means inversion of its
argument, not coefficient conjugation. On spectral polynomials,
\[
 L_nf=(c_0+a+\bar a)f
       -a(v)(-qv)^n f(Qv)
       -\bar a(v)(-qv^{-1})^n f(Q^{-1}v).
 \tag{12}
\]
The combined expression is polynomial; its apparent poles have the
original removable continuations. Its full quotient action is (3).

For \(v_j=qQ^j\), \(0\le j<N\), the finite node products and
their independently proved normals give, at each interior
transition \(j<d\), the value and first lifted jet of
\[
       \frac{A_N(t,\zeta(Qv))}{A_N(t,\zeta(v))}
                    =\frac{1+v^{-1}t}{1+Qvt}.
 \tag{13}
\]
For clarity, on the first half of the physical circle,
\[
 A_N(t,c_j)=D_j(t)^2B_j(t),\quad
 D_j(t)=\prod_{r=-j+1}^0(1+q^{-1}Q^rt),\quad
 B_j(t)=\prod_{r=j+2}^{N-j}(1+q^{-1}Q^rt),
\]
\[
 \partial_\zeta A_N(t,c_j)
                  =\frac{D_j(t)^2tB_j'(t)}{v_j-v_j^{-1}} .
 \tag{14}
\]
The normal is required only at double nodes. Multiplication by
\(v_j-v_j^{-1}\) identifies the logarithmic \(v\)-derivative
with \(tB_j'/B_j\). Removing the two end factors of \(B_j\)
gives exactly the derivative of (13). The even middle pair has
one \(B_j\) factor and reflected derivatives of opposite sign.
The odd simple middle has \(B_j=1\) and lifted derivative zero.
Inversion gives the second half. This proves the claimed interior
jets without differentiating a discrete index interpolation.

Set the cleared defect
\[
 F_t(v)=(1+Qvt)A_N(t,\zeta(Qv))
                           -(1+v^{-1}t)A_N(t,\zeta(v)).
 \tag{15}
\]
It has a double zero at each interior physical transition.
At the forward seam \(v=q^{-1}\) no homogeneous first-normal
extension of (13) is assumed. Instead \(a(v)\) has a cubic
zero there. The backward seam \(v=q\) uses the cubic zero of
\(\bar a(v)\). These zeros remove the seam defects and their
first derivatives in (12).

The coalescing coefficient poles need a separate check. For
\(\iota(v)=Q^{-1}v^{-1}\), inversion symmetry of the actual
polynomial gives the exact identity
\[
                              F_t(\iota(v))=-F_t(v).
 \tag{16}
\]
At an even-level middle pole \(v=-q^{-1}\), this involution
fixes \(v\). In the local logarithmic coordinate it changes the
sign. The matched value and first jet in (13), together with (16),
force a zero of order at least three. The simple pole of \(a\)
therefore leaves a double zero, preserving the first spectral
normal. The reflected pole is identical. At the odd physical
fixed point \(v=-1\), the paired expression leaves a zero value;
only that simple Casimir value is required. At \(N=2\), a seam
and a middle pole coincide for different shifted terms; the
cubic-zero and involution arguments apply to their respective
terms. No exceptional level is omitted.

We can now verify (10) after clearing \(M_t^{-1}\).
Its forward shifted coefficient uses
\[
 b_t(\zeta)\frac{A_N(t,\zeta(v))}
                         {A_N(t,\zeta(Qv))}
                 =(1+vt)(1+Qvt).
 \tag{17}
\]
This equality has the full jets just justified when multiplied
by the corresponding coefficient in (12). The factor on the right is
\(1-c_0t(-qv)+t^2(-qv)^2\); hence it gives the three \(L\)'s
on the right of (10). The backward term follows by inversion.
Their diagonal coefficients differ by
\[
 [b_t(\zeta)-(1-c_0t+t^2)](c_0+a+\bar a)=8t.
\]
Thus the cleared difference has every original Hermite value and
normal zero. Each combined side is polynomial, so it is divisible
by \(P_N\), proving (10) in the entire quotient.

Define the source-adapted operator
\[
             B_w=M_{w_N}L M_{w_N}^{-1}.
 \tag{18}
\]
Its scalar input normalization cancels. Since
\(R^2LR^{-2}=L_{-2}\), applying (10) twice shows that
\(b_y(Z)b_z(Z)B_w\) is a finite polynomial combination of
\(L_{-2},\ldots,L_2,Z,I\), with coefficients polynomial in
\(y,z,q,q^{-1}\). In particular all coefficients are bounded
on compact input bidisks, independently of \(N\).

For a fixed word, choose \(0<\rho_W<1\) so small that
\[
                     \rho_W C_W+\rho_W^2\le\tfrac12 ,
 \tag{19}
\]
where \(C_W\) bounds \(WZW^{-1}\) in (9). Then
\(b_t(WZW^{-1})^{-1}\) has norm at most two for
\(|t|\le\rho_W\), by its Neumann series. Conjugating the
preceding cleared formula and using (9) gives
\[
 \boxed{\qquad
 \|WZW^{-1}\|+\|WB_wW^{-1}\|\le K_W,
           \qquad |y|,|z|\le\rho_W ,
 \qquad}
 \tag{20}
\]
uniformly in \(N\). No norm of a generating unit or its inverse
was estimated separately.

## 4. Polynomial extraction from the finite head

The following construction is independent of the coherent inputs.
Assume \(D\ge1\) and \(D\le N/32\), and put \(M=2D\).
For \(0\le j\le M\), use the original kernel polynomial
\[
 K_j(\zeta)=\sum_{r=0}^j e_r(c_j)e_r(\zeta),\quad
 \ell_j=\frac{(-1)^jS_{2j}}{S_j^4},\quad
                         g_j=K_j/\ell_j .
 \tag{21}
\]
Indeed \(e_r(c_j)=0\) for \(r>j\), and
\(e_j(c_j)=S_{2j}/S_j^2\), so \(\ell_j\) is the leading
coefficient. Thus \(g_j\) is monic of degree \(j\).
The Newton recurrence immediately gives \(LK_j=c_jK_j\).

The original physical kernel row gives the exact monic recurrence
\[
 \zeta g_j=g_{j+1}+\gamma_jg_j+\beta_jg_{j-1},
 \quad
 \gamma_j=c_0+\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}}
                       +\frac{s_j^4}{s_{2j}s_{2j+1}},
\]
\[
           \beta_j=\frac{s_j^8}
                         {s_{2j-1}s_{2j}^2s_{2j+1}}>0.
 \tag{22}
\]
At \(j=0\) the last summands are zero and \(g_{-1}=0\).
To see precisely why no kernel source was lost, the ordinary
free-boundary equation for \(K_N(w,\zeta)\) has defect
proportional to \(P_N(\zeta)e_d(w)\). At the physical row
\(w=c_j\) used here, \(e_d(c_j)=0\) for \(j<d\).
The remaining row coefficients are
\[
 a_j=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\qquad
 b_j=\frac{s_j^4}{s_{2j}s_{2j+1}},
\]
so \( \zeta K_j=(c_0+a_j+b_j)K_j-a_jK_{j+1}-b_jK_{j-1}\).
Normalizing by \(\ell_j\) gives
\(-a_j\ell_{j+1}/\ell_j=1\) and
\(-b_j\ell_{j-1}/\ell_j=\beta_j\), proving (22).
All rows used are strictly before the middle.

The elementary sine bounds now imply uniform estimates
\[
 |\gamma_j|+\beta_j\le C,\qquad
       \beta_j\ge c(j/N)^4\quad(1\le j\le D),\qquad
                         \|g_j\|_{\mathrm{coeff},1}\le C^j .
 \tag{23}
\]
The last assertion follows inductively from the monic recurrence.
The indices in every denominator are at most \(4D+2<N/2\)
in the range needed below, after harmlessly excluding finitely
many initial levels. The constants are absolute.

On polynomials of degree at most \(M\), \(L\) has the distinct
eigenbasis \(g_0,\ldots,g_M\). Its exact filters are
\[
 F_j(L)=\prod_{\substack{0\le r\le M\\r\ne j}}
                     \frac{L-c_r}{c_j-c_r}.
 \tag{24}
\]
Their scalar polynomial coefficient norm satisfies
\[
                  \|F_j\|_{\mathrm{coeff},1}
                        \le e^{CD}(N/D)^{4D}.
 \tag{25}
\]
Here are the needed uniform factorials. Since
\(c_j-c_r=-s_{j+r+1}s_{j-r}\),
\[
 \prod_{r\ne j}|c_j-c_r|
 \ge(c/N^2)^M\frac{(M-j)!(M+j+1)!}{2j+1}
 \ge(c/N^2)^M\frac{(M!)^2}{2M+1}.
\]
The numerator coefficient norm in (24) is at most \(3^M\);
\(M!\ge(M/e)^M\) proves (25).

Expand a nonzero polynomial \(P\), of degree at most \(D\), as
\(P=\sum_{j=0}^D a_jg_j\). Equation (23) gives an index \(j\)
with
\[
                      |a_j|\ge e^{-CD}\|P\|_2.
 \tag{26}
\]
The written operator order in the next identity is essential:
\[
 F_0(L)Z^jF_j(L)P(Z)1
                    =a_j\left(\prod_{r=1}^j\beta_r\right)1.
 \tag{27}
\]
The right filter first isolates \(a_jg_j\). In \(j\) steps
of (22), the only path from index \(j\) to zero lowers at
every step. Its coefficient is the displayed product.
All intermediate degrees are at most \(2D=M\), so the final
filter is exact. No high-degree quotient or uncontrolled
complement enters this calculation.

Moreover (23) and the factorial inequality imply
\[
 \left(\prod_{r=1}^j\beta_r\right)^{-1}
       \le e^{CD}(N/D)^{4D},\qquad 0\le j\le D .
 \tag{28}
\]
For \(j>0\), first bound this by
\(e^{Cj}N^{4j}/(j!)^4\); then use the monotonicity of
\(j\log(N/j)\) for \(j\le D\le N/32\).
The empty product at \(j=0\) is one.

Consequently there is an explicit noncommutative polynomial
\(\mathscr A_{P,N}(Z,L)\) such that
\[
 \mathscr A_{P,N}(Z,L)P(Z)1=1,\qquad
 \deg\mathscr A_{P,N}\le5D,\qquad
 \|\mathscr A_{P,N}\|_{\mathrm{coeff},1}
       \le\frac{e^{CD}(N/D)^{12D}}{\|P\|_2}.
 \tag{29}
\]
It is exactly the left side of (27) divided by its nonzero
scalar on the right. The three losses in (29) are the two
filters, the inverse lower-path coefficient, and the factor
in (26). They use only finite explicit source data.
No singular-value decomposition or unspecified inverse is used.

## 5. The joint transported Gram bound

Fix a word \(W\), and take \(\rho_W\) from (19).
There are \(C_W<\infty\) and \(N_0\) such that, for
\[
 N\ge N_0,\quad 1\le D\le N/32,\quad
 |y|,|z|\le\rho_W,\quad \deg P\le D,
\]
the full original vectors obey
\[
 \boxed{\begin{aligned}
 &e^{-C_WD}(D/N)^{24D}\|P\|_2^2\,\|Ww_N\|^2\\
 &\hspace{12mm}\le\|WP(Z)w_N\|^2
       \le e^{C_WD}\|P\|_2^2\,\|Ww_N\|^2 .
 \end{aligned}}
 \tag{30}
\]
Constants do not depend on \(D,N,P,y,z\) in this range.
For \(D=0\) both sides are exactly
\(|P|^2\|Ww_N\|^2\). The zero polynomial is included trivially.

For the lower bound conjugate (29) by the actual invertible
operator \(\mathcal U=WM_{w_N}\). Since multiplication by
\(w_N\) commutes with \(Z\), its two conjugated generators are
\[
        Z_{\mathcal U}=WZW^{-1},\qquad
        L_{\mathcal U}=WB_wW^{-1}.
 \tag{31}
\]
Their norms are bounded by (20). Thus the conjugated extraction
operator has norm at most
\(e^{C_WD}(N/D)^{12D}/\|P\|_2\).
It maps \(WP(Z)w_N\) exactly to \(Ww_N\).
Squaring the resulting inequality proves the lower bound.
For the upper bound use
\[
 WP(Z)w_N=P(WZW^{-1})Ww_N
\]
and the uniform bound (9). The factor \(\sqrt{D+1}\)
from coefficient Cauchy--Schwarz is absorbed in \(e^{C_WD}\).
No condition number of \(\mathcal U\), \(W\), or \(M_{w_N}\)
appears in this proof.

In particular, if \(D_N=o(N)\) and \(P_N^{\rm obs}\) has
degree at most \(D_N\) and coefficient norm one, then
\[
 \boxed{\qquad
 \frac1N\log
 \frac{\|WP_N^{\rm obs}(Z)w_N(y,z)\|^2}{\|Ww_N(y,z)\|^2}
                             \longrightarrow0
       \quad(|y|,|z|\le\rho_W).
 \qquad}
 \tag{32}
\]
The convergence is uniform on the displayed bidisc.
Indeed \(D_N+D_N\log(N/D_N)=o(N)\).
A nonzero scalar coefficient norm with logarithm \(o(N)\)
may also be included by homogeneity.

The denominator is the norm of the newly transported packet.
Equation (32) does not say that it has the old packet's rate.
For example \(w_N(0,0)=R^2/N\), while
\(R^{-1}w_N(0,0)=R/N\) has squared Newton norm \(1/N\).
The theorem compares observations of each such transported
packet with that same packet, and is consistent with this change.

## 6. Original closing and complete proof sources

Every operation in the argument is an identity on the full
original algebra. The low polynomial head is used only to
construct the extraction operator; its conjugate acts on the
full transported packets. No physical normal or source direction
has been declared invisible.

The original marked row \(\ell_N\) may be applied unchanged.
For example extraction gives the exact equality
\[
 \ell_N(Ww_N)=
 \ell_N\!\left[
    \mathscr A_{P,N}(Z_{\mathcal U},L_{\mathcal U})
                              WP(Z)w_N\right].
 \tag{33}
\]
It does not replace this row by a positive norm, or prove
a lower bound for \(\ell_N(WP(Z)w_N)\).
The action of the new packet and its specified scalar closing
remain separate questions.

The result concerns fixed linear words of crossings and genuine
turns and a word-dependent small coherent input bidisc. It does
not give a closed bounded lift through arbitrary branching
subtrees. Nor does sublinear Casimir degree mean a bounded number
of crossings or degree four of a variational objective.
No new knot-volume identity or finite-exception theorem is asserted.

All four complete matching proof sources were read:

| Source | SHA-256 |
|---|---|
| [Full generating tensor, 482 lines](research_centered_fourier_full_tensor_source.md) | 8426410354feb509c2780e1207613899bda8ab5eb46ad22fd4ab008bf5841bf1 |
| [Full crossing/AW transport, 1283 lines](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_current_free_aw_crossing_transport.md) | f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a |
| [Finite-band conjugation, 730 lines](research_unit_turn_finite_band_branching_operator.md) | 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb |
| [Full kernel difference source, 399 lines](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_edge_kernel_difference_and_endpoint_bound.md) | 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da |

The first supplies the exact generating unit and its physical
value/normal products. The second supplies the full AW operators,
their endpoint mechanism and exact word conjugation. The third
supplies the verified tridiagonal base matrix in (6). The fourth
supplies the original physical kernel row and its retained free
source. The generating-unit gauge identity, uniform coefficient
extraction and joint Gram bound are proved above.
No general Hilbert--Schmidt equivalence, generic orthogonality
measure, or unverified root-of-unity limit is imported.
Only written mathematics and text operations were used; earlier
finals and public manuscripts remain unchanged.
