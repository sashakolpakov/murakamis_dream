# A polynomial normal gap at the original marked boundary

24 November 2026. Written research proof.

The original marked boundary selects a particular path block of an
actual adjacent-crossing difference equation. Its left and right
eigenvectors are explicit finite products. They turn the normal
operator into a complex weighted path Laplacian, whose compatible
inverse has polynomial norm. No positivity of the complex weights
is assumed. In the already specified positive height metric the
normal gap is at least \(c_0N^{-12}\).
Here normal means transverse to the specified vector line,
not a Casimir derivative or a moving-level normal.

This controls the part transverse to the marked boundary mode.
It leaves that mode's amplitude free and does not bound the original
closed scalar below. In particular, an interior crossing with the
opposite sign still requires a signed overlap between different
normal operators.

## 1. The original source and the statement

Fix \(N\ge2\), and use the conventions of the complete inputs:
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad c=1+q,\quad
 x=-q^{-1},\quad \kappa=q^{d^2/2},\quad F_a=(Q;Q)_a .
 \tag{1}
\]
In particular \(F_d=N\). Write
\(\mu_j=Q^j+qQ^{-j}\), \(0\le j<N\), for the distinct coideal roots,
and \(p_N\) for their monic polynomial. They are the sorted roots
\(2\sqrt q\cos\alpha_r\), with
\(\alpha_r=(r+\tfrac12)\pi/N\), in a different order. All indices
on \(\mu_j\) are read modulo \(N\).

The finite continuants and their generating polynomial are
\[
 \begin{split}
 D_{-1}&=0,\quad D_0=1,\\
 D_{a+1}(\lambda;\sigma)
   &=(\lambda+qQ^a\sigma)D_a(\lambda;\sigma)
                   -q(1-Q^a)^2D_{a-1}(\lambda;\sigma),\\
 \Phi_{\lambda,\sigma}(z)&=\sum_{a=0}^d
                       D_a(\lambda;\sigma)z^a/F_a .
 \end{split}                                                    \tag{2}
\]
Only \(F_a\) with \(a<N\) occurs in a denominator.

For four physical heads the literal row is
\((\ell_{12}\otimes m_{34})R_{23}^+\), with the last marked cap
in its original position. On the external channel \(\mathcal E_c\),
its last height is \(\mu_*=-q^{-1}-q^2\). Its other two input
heights are \(\nu,\rho\), and [C] gives
\[
 M^+_{\nu,\rho}
   =\beta_N\overline{\Phi_{\rho,\nu}(q^{-1})}
   =\beta_N\Phi_{\nu,\rho}(-q),\qquad
 \beta_N=\frac{T_*}{A_c}\frac{\kappa(1-q)}2 .
 \tag{3}
\]
Here \(A_c,T_*\) are the original nonzero boundary constants.
The second equality is continuant reciprocity, including the
conjugation of \(F_a\). Neither \(\beta_N\) nor a further original
external factor \(\chi_N\) is deleted from the source.

Fix \(\rho=\mu_l\), put \(m=\lfloor N/2\rfloor\), and define
\[
 t(j)=
 \begin{cases}[m-j]_N,&N\text{ even},\\[m+j]_N,&N\text{ odd},
 \end{cases}
 \qquad I_l=\{j:l\le t(j)\le d\},\qquad M_l=N-l .             \tag{4}
\]
The selected set is ordered by \(t=l,\ldots,d\). It is precisely
the nonzero support of the boundary column in (3); in this order
its path is \(l\longleftrightarrow l+1\longleftrightarrow
\cdots\longleftrightarrow d\).

We construct below an actual adjacent-crossing matrix \(J_{c,\rho}\).
The set \(I_l\) is a reducing path block for this matrix. Write
\(J_l\) for its restriction, and use counting Euclidean norms in
these raw height coordinates. There are explicit nonzero vectors
\(s_l\) and rows \(r_l\) with
\[
 r_l(J_l-\mu_*I)=0,\quad (J_l-\mu_*I)s_l=0,\quad
 r_ls_l=\frac{2\kappa}{1-q^3}.
 \tag{5}
\]

**Theorem.** There is a universal \(C>0\) such that
\[
 \operatorname{dist}_2(w,\mathbb Cs_l)
       \le CN^{11}\|(J_l-\mu_*I)w\|_2 .                       \tag{6}
\]
Every compatible right side \(f\), meaning \(r_lf=0\), has an
explicit solution of \((J_l-\mu_*I)w=f\) with
\(\|w\|_2\le CN^{11}\|f\|_2\).
In [H]'s original absolute-height metric, restricted to this block,
\[
 \operatorname{dist}_{\rm ht}(w,\mathbb Cs_l)
       \le CN^{12}\|(J_l-\mu_*I)w\|_{\rm ht}.                 \tag{7}
\]
The constants are independent of \(l\), all selected coordinates,
and \(N\). For \(M_l=1\) the compatible right side is zero.
This is a normal equation on the specified block, not a claim that
an arbitrary braid preserves that block.

## 2. A finite cyclic difference equation

Let \(T_\rho\) be the actual one-head tridiagonal matrix
\[
 (T_\rho v)_a=(1-Q^a)v_{a-1}
       +q(1-Q^{a+1})v_{a+1}-qQ^a\rho v_a .
 \tag{8}
\]
The endpoint coefficients vanish at \(a=0,d\). Its eigenmatrix is
\[
 (U_\rho)_{a,j}=q^{-a}D_a(\mu_j;\rho)/F_a,\qquad
 T_\rho U_\rho=U_\rho X,\quad X=\operatorname{diag}(\mu_j).
 \tag{9}
\]
It is invertible by the full simple-root graph construction in [K].
No bound for \(U_\rho^{-1}\) is used in the theorem.

Here is a finite proof of the needed difference relation. Put
\(u=Q^j,v=q/u\), and define
\[
 \begin{split}
 a_j&=-\frac{v^2+q\rho v+qQ}{(u-v)(v-Qu)},\\
 b_j&=\frac{u^2+q\rho u+qQ}{(u-v)(u-Qv)},\\
 (\mathscr D_\rho f)_j
       &=a_j(f_{j+1}-f_j)+b_j(f_{j-1}-f_j).
 \end{split}                                                   \tag{10}
\]
Every denominator factor is a unit phase times a difference of
odd powers of \(q\), and is nonzero at all levels in question.

The recurrence (2), including its final row \(D_N=0\), gives
\[
 (1-\mu_jz+qz^2)\Phi_{\mu_j,\rho}(z)
       =(1+q\rho z+qQz^2)\Phi_{\mu_j,\rho}(Qz).
 \tag{11}
\]
In particular its coefficients below \(z^N\), with constant one,
are unique, since \(1-Q^a\ne0\) for \(0<a<N\). Applying this
uniqueness after shifting \(j\) gives the formal ratios
\[
 \frac{\Phi_{\mu_{j+1},\rho}(z)}{\Phi_{\mu_j,\rho}(z)}
       \equiv\frac{1-uz}{1-vz/Q},\qquad
 \frac{\Phi_{\mu_{j-1},\rho}(z)}{\Phi_{\mu_j,\rho}(z)}
       \equiv\frac{1-vz}{1-uz/Q}\pmod {z^N}.                  \tag{12}
\]
For example the first rational multiplier changes the two
denominator roots \(u,v\) to \(Qu,v/Q\) in (11). All these formal
denominators have constant one.

Substitute (12) into (10) and take a common denominator.
The resulting identity is
\[
 a_j\left(\frac{1-uz}{1-vz/Q}-1\right)
 +b_j\left(\frac{1-vz}{1-uz/Q}-1\right)
  =\frac{1+q\rho z/Q+qz^2/Q}
         {(1-uz/Q)(1-vz/Q)}-1 .
 \tag{13}
\]
The right side is
\(\Phi_{\mu_j,\rho}(z/Q)/\Phi_{\mu_j,\rho}(z)-1\) by (11).
Coefficient comparison proves, for every \(0\le a<N\),
\[
 \mathscr D_\rho\bigl(D_a(\mu_j;\rho)/F_a\bigr)
    =(Q^{-a}-1)D_a(\mu_j;\rho)/F_a .
 \tag{14}
\]
Thus, with \(Z=\operatorname{diag}(Q^a)\) on the physical head,
\[
 K_\rho:=U_\rho^{-1}Z^{-1}U_\rho=I+\mathscr D_\rho^{\mathsf T}.
 \tag{15}
\]
The transpose is important: (14) acts on a row of \(U_\rho\).
This is a cyclic tridiagonal matrix, with the coincident shifts
at \(N=2\) interpreted by addition.

The relation is a finite version of the usual
Al-Salam--Chihara difference equation; that general mechanism is
not claimed new. Equations (11)--(14) supply its proof and exact
root conventions here without importing an analytic extension.

## 3. The actual adjacent crossing and its selected path

Let \(\mathcal D=\operatorname{diag}(q^{-a})\). The actual
positive crossing in the unchanged height frame is
\[
 B^+_{c,\rho}=\kappa U_\rho^{-1}\mathcal D\overline{U_c},
 \qquad B^-_{c,\rho}=\overline{B^+_{c,\rho}}
                         =(B^+_{c,\rho})^{-1}.              \tag{16}
\]
These are the source matrices of [S,T], not arbitrary connections.
The corresponding physical output operator is
\[
 (J_c'v)_a=(1-Q^{-a})v_{a-1}
 +q(1-Q^{-a-1})v_{a+1}-q^{-1}Q^{-a}cv_a .
 \tag{17}
\]
Define \(J_{c,\rho}=U_\rho^{-1}J_c'U_\rho\) at every \(N\).
It obeys
\[
 J_{c,\rho}B^+_{c,\rho}=B^+_{c,\rho}X,\qquad
 B^-_{c,\rho}J_{c,\rho}=XB^-_{c,\rho}.                        \tag{18}
\]

For \(N\ge3\) it has a directly sparse height formula:
\[
 J_{c,\rho}
 =-\frac{K_\rho X+XK_\rho+2q\rho I}{1+Q}
                                      -q^{-1}cK_\rho .       \tag{19}
\]
Indeed, decompose (8) into its lower arrow, upper arrow and
diagonal. Multiplication by \(Z^{-1}\) in (17) gives
\((1+Q)J_c'=-(Z^{-1}T_\rho+T_\rho Z^{-1}+2q\rho I)
-q^{-1}c(1+Q)Z^{-1}\), entry by entry. Conjugation proves (19).
Here \(|1+Q|\ge1\), so no large division occurs.

The two directions on the edge \(j,j+1\) have the same extra
factor:
\[
 (J_{c,\rho})_{j,j+1}=b_{j+1}h_j,\quad
 (J_{c,\rho})_{j+1,j}=a_jh_j,\quad
 h_j=-q^{-1}(\mu_{-j}+c)
       =-q^{-1}(1+Q^j)(q+Q^{-j}).
 \tag{20}
\]
For \(\rho=\mu_l\), \(a_j\) and \(b_{j+1}\) vanish at the
same single edge \(j=t(l)\). To check both parities explicitly,
the numerator of \(a_j\), up to a unit, factors as
\((1+Q^{j+l})(1+qQ^{j-l})\). At even \(N\) only the first
factor can vanish, at \(j=m-l\); at odd \(N\) only the second
can vanish, at \(j=m+l\). The factors for \(b_{j+1}\) give
the same edge. The additional factor \(h_j\) vanishes precisely
at \(j=m=t(0)\). These are two cuts of the cycle, with
coincident cuts allowed. There is no one-way edge left at a cut.

The support \(I_l\) in (4) is one of the resulting path blocks.
For \(l=0\) it is the whole cycle opened at its one cut.
For \(l=d\) it is a singleton. Every internal edge is nonzero.
The cut coefficients were zero in the original operator, so
passing to this path discards no cycle current at its endpoints.
The elementary root-grid bound for a nonzero factor
\(1-q^h\) or \(1+q^h\) is \(c_0/N\). The numerator factors
above and denominators of modulus at most four therefore give
\[
 c_0N^{-4}\le |(J_l)_{i,i+1}|,\ |(J_l)_{i+1,i}|
                    \le CN^2\qquad(0\le i<M_l-1).
 \tag{21}
\]
Indices \(i\) here refer to the ordered path, not the cyclic labels.
The upper bound also uses that the denominators in (10) have
modulus at least \(c_0N^{-2}\). No lower joint-frame bound enters.

## 4. The exact marked left and right modes

Let \(r_j=\Phi_{\mu_j,\rho}(-q)\). Reciprocity gives the first
equality in (3). The cumulative product of [C] now says
\[
 r_j=\overline{U_{t(j)}V_l}\quad(j\in I_l),\qquad r_j=0
       \quad(j\notin I_l),
 \tag{22}
\]
where \(U,V\) are exactly [C]'s finite product factors.
Their bounds \(1\le|U_t|\le C\sqrt N\) and
\(c_0N^{-1/2}\le|V_l|\le N\) show
\[
 c_0N^{-1/2}\le |r_j|\le CN^{3/2}\quad(j\in I_l).
 \tag{23}
\]

Here is an exact normalization of the modes. Put
\(w_a=(-Q)^a\). By (9), \(r=w^{\mathsf T}U_\rho\), so (16) gives
\[
 rB^+_{c,\rho}
       =\kappa\bigl(\overline{\Phi_{\mu_j,c}(-Q^{-1})}\bigr)_j
       =\frac{2\kappa}{1-q^3}\,e_*^{\mathsf T}.
 \tag{24}
\]
The last finite product contains \((1;Q)_B\); it vanishes
unless \(B=0,A=d\), precisely the label \(\mu_*\).
At that label its unconjugated value is
\((q^{-1};Q)_d=2/(1-q^{-3})\).
Thus (24) is the ordinary same-sign cap slide, with its actual scalar.
Combining (18) and (24) proves \(rJ_{c,\rho}=\mu_*r\).

The right mode is \(s=B^+_{c,\rho}e_*\). The graph inverse from
[K] gives the entries explicitly:
\[
 s_j=\kappa\,\frac{E_d(\mu_j;\rho)}{p_N'(\mu_j)}\,r_j .
 \tag{25}
\]
In fact \(D_a(c;\mu_*)=q^aF_a\); reciprocity implies
\(D_a(\mu_*;c)/F_a=(-q^{-1})^a\), and hence
\(\mathcal D\overline{U_c}e_*\) has entries \((-q)^a\).
The inverse row of \(U_\rho\) is
\((E_d/p_N')\,(D_a/F_a)_a\), proving (25).

The same continuant reflection and determinant identity as in
[K,S] give, for any two of these rotated-real roots,
\[
 E_d(\lambda;\rho)=q^d\overline{D_d(\lambda;\rho)},\quad
 D_dE_d=q^dN^2,\quad
 \left|\frac{E_d(\lambda;\rho)}{p_N'(\lambda)}\right|
                                            =\sin\alpha_\lambda .
 \tag{26}
\]
One can check the reflection directly: conjugate the leading
minor, multiply each row by \(q\), and reverse its order.
The diagonals and adjacent-arrow products become those of the
trailing minor. The derivative formula is
\(|p_N'(\lambda)|=N/\sin\alpha_\lambda\).
Consequently \(s\) has exactly the support \(I_l\), and
\[
 c_0N^{-3/2}\le|s_j|\le CN^{3/2},\qquad
 rs=w^{\mathsf T}U_\rho B^+e_*
     =\kappa\sum_{a=0}^d q^{3a}
     =\frac{2\kappa}{1-q^3}.                                  \tag{27}
\]
This pairing is bilinear, not a positive inner product.
Since \(|rs|=\csc(3\pi/(2N))\ge c_0N\), the known mode
projector \(\Pi=sr/(rs)\) has norm at most \(CN^3\).
Its normalization is not chosen from an unknown closed source value.

For clarity, \(N=2\) needs no division by \(1+Q\). Here
\(q=i,c=\mu_*=1+i\). At \(\rho=c\), direct use of (8),(17) gives
\[
 J_{c,c}=\begin{pmatrix}3c&4i\\-4&-3c\end{pmatrix},
 \quad r=(2,c),\quad s=\kappa(1-i,i)^{\mathsf T}.
 \tag{28}
\]
Their pairing is \(\kappa(1-i)=2\kappa/(1-q^3)\).
At \(\rho=-c\), \(J=X\), the selected block is \(j=0\),
and its modes are \(r=1-i,s=\kappa\).
Thus all assertions above hold after enlarging universal constants.

## 5. Compatible elimination by first differences

Restrict now to the selected ordered block. Write
\(L_l=J_l-\mu_*I\), \(D_r=\operatorname{diag}(r_i)\),
\(D_s=\operatorname{diag}(s_i)\), and
\[
 \omega_i=r_i(L_l)_{i,i+1}s_{i+1}\quad(0\le i<M_l-1).
 \tag{29}
\]
Every \(\omega_i\) is nonzero, with
\(c_0N^{-6}\le|\omega_i|\le CN^5\), by (21),(23),(27).
The two null equations imply
\[
 D_rL_lD_s=-\nabla^{\mathsf T}
                    \operatorname{diag}(\omega_i)\nabla,\qquad
 (\nabla y)_i=y_{i+1}-y_i .                                  \tag{30}
\]
Here is a proof including the endpoints. The left side has zero
row and column sums. At its first vertex these equalities force
the two off-diagonal entries across the first edge to agree.
Induction does the same at every following edge. Each diagonal
is minus the sum of its incident edge weights, giving (30).
Equivalently, the difference between the forward and backward
flux is constant along the path and vanishes at its end.

This factorization is complex symmetric; it is not a positive
quadratic form. Nevertheless \(\nabla\) maps the counting
orthogonal complement of the constant vector bijectively onto
\(\mathbb C^{M_l-1}\), with least singular value
\(2\sin(\pi/(2M_l))\ge c_0/N\).
Its transpose maps that space back bijectively. Thus the
restriction of the right side of (30) to constants perpendicular
is invertible and its inverse norm is at most \(CN^8\).
This is a product bound for three invertible maps between the
stated spaces; it does not infer positivity from complex weights.

There is also a direct flux solution. For \(r_lf=0\), set
\[
 g_i=r_if_i,\quad
 F_i=\sum_{a=0}^i g_a,\quad
 y_{i+1}-y_i=F_i/\omega_i,\quad \sum_{i=0}^{M_l-1}y_i=0 .
 \tag{31}
\]
The compatibility condition says \(\sum_i g_i=0\). It is exactly
the last-vertex equation, not an additional imposed endpoint
value. There is no requirement \(y_{M_l-1}=0\).
The vector \(w=D_sy\) solves \(L_lw=f\). For a singleton
the compatible datum and this chosen solution are both zero.

The inverse bound for (30) and the upper component bounds yield
\[
 \|w\|_2\le
 \|D_s\|\,CN^8\,\|D_r\|\,\|f\|_2
                  \le CN^{11}\|f\|_2 .                       \tag{32}
\]
Also (30) proves \(\ker L_l=\mathbb Cs_l\) and
\(\operatorname{range}L_l=\ker r_l\), without a rank guess.
For arbitrary \(w\), apply (32) to \(f=L_lw\);
subtracting the constructed solution changes \(w\) by a kernel
vector. This proves (6).

At fixed neighboring heights all other factors in [H]'s complete
height metric are a common scalar. Its remaining weights are
\(\csc\alpha_j\), between \(1\) and \(CN\).
The change from counting norm to this prescribed norm costs
at most \(C\sqrt N\). Equation (32) therefore gives the clean
uniform exponent \(12\) in (7). No physical Hilbert--Schmidt
frame comparison is used.

There is also a unique gauge that preserves the marked row.
The projector \(\Pi=s_lr_l/(r_ls_l)\) satisfies
\[
 \|\Pi\|_2\le CN^3,\quad \|\Pi\|_{\rm ht}\le CN^{7/2},
 \qquad
 \|(I-\Pi)w\|_{\rm ht}
          \le CN^{15}\|L_lw\|_{\rm ht}.                       \tag{32a}
\]
Indeed choose a best raw approximation to \(w\) on its \(s_l\)
line, and apply \(I-\Pi\) to their difference. Equation (6)
and \(\|I-\Pi\|_2\le CN^3\) give raw cost \(CN^{14}\);
the height change contributes at most \(C\sqrt N\).
For \(r_lf=0\), applying \(I-\Pi\) to (31)'s solution gives
the unique solution of \(L_lw=f,\ r_lw=0\), with this bound.

Write \(H_{\rm ht}\) for the restricted height Gram. The explicit
positive marked Gram is
\[
 H_{\rm mark}=\Pi^\dagger H_{\rm ht}\Pi
                   +(I-\Pi)^\dagger H_{\rm ht}(I-\Pi),
 \qquad
 \tfrac12H_{\rm ht}\le H_{\rm mark}\le CN^7H_{\rm ht}.        \tag{32b}
\]
The lower bound follows by adding the two components of \(w\)
and using the triangle inequality; the upper follows from (32a).
It makes \(\mathbb Cs_l\) orthogonal to \(\ker r_l\), and equals
\(H_{\rm ht}\) exactly on each of those two subspaces.
Thus the row \(r_l\) is retained as the known marked coordinate,
not replaced by a new functional. Both \(L_lw\) and
\((I-\Pi)w\) lie in \(\ker r_l\), so (32a) holds in
\(H_{\rm mark}\) as well. Its left side is then the exact
orthogonal distance to the mode. Nonzero scalar rescalings of
the original marked row do not change \(\Pi\).

## 6. What this eliminates in the original source

The coefficients in (31) are all known finite source data.
The compatible normal problem can therefore be eliminated
by cumulative sums and first differences with polynomial loss.
Its residual energy remains quadratic in that linear problem.
It does not require a dense inverse with an unknown condition
number, or an estimate for a discarded boundary coordinate.
At greater fixed width the earlier ordinary caps and their
constraints remain exactly those of [C,H]; the same local block
calculation has the same constants.

This selected normal problem still applies to every attached state
at the literal boundary. Let \(P_l\) be coordinate projection onto
\(I_l\). It commutes with \(J\), has height norm one, and
\(r=rP_l\). Thus \(rw=rP_lw\) for any full incoming height vector,
and the gap applies to \(P_lw\) with residual
\(P_l(J-\mu_*I)w\). The whole preceding word remains in \(w\).
This does not permit inserting \(P_l\) before other crossings or
give a bound for the unselected component.

The one-dimensional kernel remains. Its coefficient is not
controlled by a normal residual and has not been fixed by
minimization. The original marked row, its factor \(\beta_N\),
and the original exterior factor \(\chi_N\) must still be used
when recovering the scalar.

The unresolved opposite-sign seam is explicit. Conjugating
(18) gives \(q\overline J\,B^-=B^-X\), whereas the marked
row is a left mode of \(J\). More concretely, if
\(f_\rho(z)=(\Phi_{\mu_j,\rho}(z))_j\) and
\(g_\rho(z)=f_\rho(z)B^-\), then the literal opposed row is
\(\beta_Ng_\rho(-q)\), and (11),(18) give
\[
 g_\rho(z)J=(z^{-1}+qz)g_\rho(z)
                -(z^{-1}+q\rho+qQz)g_\rho(Qz).                \tag{33}
\]
No lower bound for that signed mode overlap is proved here.
Nor is \(I_l\) declared invariant under arbitrary crossings.
These are full coideal source coordinates; no Casimir first
normal, original cap, or boundary phase has been replaced.

The general difference equation and cap slide are established
mechanisms. The additional assertion is the polynomial normal
gap on the block selected by the actual marked boundary,
with its explicit compatible flux inverse and existing height
metric. The older pivotal-cap reassociation [P] is a different
source-basis reduction. The positive Jacobi boundary problem [J]
concerns Newton value data in a spectral half-plane and its
positive Green resolvent. Here the operator is non-Hermitian,
the data are the marked coideal mode, and the estimate holds
on every selected path without a half-plane assumption.
Neither result supplies a lower bound
for a prescribed coherent exterior or the finite-exception
volume theorem after arbitrary short partial fillings.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| C | [Cumulative marked boundary](research_coideal_cap_straddling_cumulative_kernel.md) | 450 | 3ff48e5998f325e1391c088b688a01388f5b8e21d3c8ce53f9ed556e9b289c71 |
| H | [Height pairing and original boundary](research_coideal_height_pairing_and_marked_boundary.md) | 543 | bed81fcb12b20d16d41c55b476b13d8d69b1fe79d0d0620c31230ba652b1d82f |
| S | [Signed crossing and exact phases](research_coideal_crossing_signed_volume_chamber.md) | 634 | 7bf6fb943d2c8080875375c4529776159fc72fbde2e5d8a7d0742e0cbdb10fc0 |
| T | [Actual coideal crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| K | [Continuant source kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |
| P | [Original pivotal cap reassociation](actual_pivotal_cap_reassociation_angle_packet.md) | 243 | c822bbcc34b86c600f291f7e66c210253f341319a9d92007fcc51e6633424b14 |
| J | [Earlier positive Jacobi charge boundary](research_physical_jacobi_charge_boundary.md) | 432 | 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583 |

Only written mathematics and text/hash operations were used.
Earlier final notes, the ledger, and public manuscripts are unchanged.
