# A finite matrix test for the microscopic main-meridian profile

The main meridian is the small loop linking the knot once. Write its eigenvalue as $M$, and let $f_N(Y)$, with $Y=M^2$, be the reduced ADO knot invariant at level $N$. The value $f_N(1)$ is the complete-color scalar. A volume theorem for that scalar does not by itself control $f_N$ when the meridian moves: zeros can approach $M=1$ at distance of order $1/N$.

This note gives a conditional way to control the smaller deformation $Y=e^{z/N}$, with $z$ in a fixed complex disk. Its input is a specified difference operator obtained from the actual finite cut formula, together with the first variation of that same formula in the quantum parameter. Retaining this variation matters: the operator at the root of unity alone loses the central direction in which the meridian profile varies.

The algebraic reduction proved below has a bounded size. The number of free central coordinates is at most the fixed shift order of the operator, and the actual cut formula bounds their Laurent degrees independently of $N$. The first variation therefore gives a linear system with a bounded number of rows and columns. A uniform lower bound for its smallest singular value, together with an explicit condition on the reconstruction frame, implies boundedness of the normalized regular meridian profile. An alternative criterion uses a regular-singular differential equation and finitely many resonance tests.

Under either criterion, the regular remainder and the reduced invariant have the same leading logarithmic growth as $f_N(1)$ on a smaller fixed $z$-disk. For a knot covered by the complete-color volume theorem, this growth is the volume of that same knot complement. The matrix and regular-singular estimates are hypotheses: this note does not prove them for every knot in the covered class, and it does not assume that the normalized profile converges to one.

## 1. The specified state and the additional operator input

Fix a knot, its zero-framed finite cut, and its actual reduced even ADO state. Write

\[
q_N=e^{\pi i/N},\qquad Q_N=q_N^2,\qquad Y=M^2,\qquad U=Y^N,
\qquad K_N=f_N(1).
\tag{1}
\]

Assume the scalar result for this knot gives $N^{-1}\log|K_N|\to v>0$. All normalizations below are therefore defined for sufficiently large levels. The [ordinary-color pointing and its polynomial bound](regularized_kashaev_period.md) give

\[
 f_N(Q_N^j)=C_j(q_N)\quad(1\le j<N),\qquad
 |C_j(q_N)|\le D_N,\qquad ND_N/|K_N|\longrightarrow0.
\tag{2}
\]

The [actual crossing support](relative_octahedral_period.md) and its [Laurent-degree bound](actual_ado_complete_meridian_zero_accumulation.md) give an interval of integer carries $k_-\le k\le k_+$, independent of level, such that

\[
 f_N(Y)=\sum_{t=0}^{N-1}Y^t f_{t,N}(U),\qquad
 f_{t,N}(U)=\sum_{k=k_-}^{k_+}c_{k,t,N}U^k.
\tag{3}
\]

The interval can be enlarged to cover finitely many small levels. Its existence follows term by term from the actual Laurent support bound, and does not estimate the signed coefficients $c_{k,t,N}$.

Retain a specified whole finite-cut preoperator

\[
 \mathcal A(q,Z,Y,S)=\sum_k a_k(q,Z,Y)S^k,
 \qquad (S_q F)(Y)=F(q^2Y),
\tag{4}
\]

and its supplied finite lift $G_N(q,Y)$, with

\[
 \mathcal A(q,q^N,Y,S_q)G_N(q,Y)=0,
 \qquad G_N(q_N,Y)=f_N(Y).
\tag{5}
\]

Work over $\mathbb C(q)$; no descent of an arbitrarily chosen minimal operator to $\mathbb C(q^2)$ is assumed. The [squared-meridian finite-sum construction](even_meridian_norm_descent.md), using the [finite-sum annihilator argument](finite_sum_annihilator.md), supplies one whole lift and preoperator over $Q=q^2$. For that choice, (4) is obtained by substituting $Q=q^2$ and replacing its central variable $Q^N$ by $Z^2$. Thus (5) is available constructively from the finite source. The formulas below also allow a specified whole preoperator over the larger field.

Clear fixed denominators and make a fixed Laurent shift normalization before using (4). Suppose all $Y$ exponents in its coefficients lie in $[-D,D]$, with $D$ independent of $N$. Terms that vanish at $Z=-1$ are retained. The nonzero root specialization

\[
 P_N=\mathcal A(q_N,-1,Y,S_{Q_N})
\tag{6}
\]

has a fixed shift width $w$, and both endpoint coefficients are nonzero rational functions of $Y$, outside finitely many levels. We may shift its first nonzero index to zero. The whole preoperator can have larger order than this root specialization.

These are supplied-operator data, not coefficients reconstructed from unknown values of $f_N$. The first-normal coefficient $\partial_Z\mathcal A$ is additional to the root operator: replacing $\mathcal A$ by $\mathcal A+(Z+1)B$ leaves (6) unchanged but changes the first-normal rule. A fixed pointing of (6) alone does not specify that rule. Such a replacement need not annihilate the same actual finite lift.

## 2. The exact residue-coordinate normal equation

Use the actual first-order deformation

\[
 q=q_N\left(1+\frac{\epsilon}{2N}\right),\qquad
 q^2=Q_N\left(1+\frac{\epsilon}{N}\right),\qquad
 Z=q^N=-\left(1+\frac\epsilon2\right),\qquad \epsilon^2=0.
\tag{7}
\]

The sign of the $Z$ derivative in this coordinate is consequently negative. If (4) came from a $Q^N$ variable, the chain rule for $Z^2$ gives its usual positive derivative instead.

Every rational function of $Y$ has a unique expression in the basis $1,Y,\ldots,Y^{N-1}$ over $\mathbb C(U)$. For a residue coordinate $h_t(U)$, the $k$th shift has the exact expansion

\[
 S_q^k\bigl(Y^t h_t(U)\bigr)
 =Q_N^{kt}Y^t\left[h_t(U)+
 \epsilon k\left(\frac tN h_t(U)+U h_t'(U)\right)\right].
\tag{8}
\]

Let $L_N(U)$ be the $N\times N$ matrix of (6) in this basis. Let $C_N(U)$ be the matrix of $\sum_k k a_k(q_N,-1,Y)S_{Q_N}^k$. Finally set

\[
 J_N(U)=
 \operatorname{Mat}\!\left(
 \sum_k\left[\frac{q_N}{2N}\partial_q a_k
              -\frac12\partial_Z a_k\right]_{q_N,-1}
                    S_{Q_N}^k\right)
       +C_N(U)\operatorname{diag}_{0\le t<N}(t/N).
\tag{9}
\]

At the actual root, the microscopic shift $Y=e^{z/N}\mapsto Q_NY$ is exactly $z\mapsto z+2\pi i$. It is not a small translation in $z$. The differential term in (8) comes from varying the supplied quantum parameter through (7), not from an invalid small-step Taylor expansion of the root shift.

All shifts in the first term are retained, including those whose root coefficients vanish. Write the first-order lift of (3) as the coordinate vector $\mathbf f_N+\epsilon\mathbf g_N$. Expanding (5), using (8), proves

\[
 L_N\mathbf f_N=0,\qquad
 L_N\mathbf g_N+C_N U\mathbf f_N'+J_N\mathbf f_N=0.
\tag{10}
\]

This is a direct residue-basis form of the [source-corrected first quantum-normal equation](source_corrected_quantum_normal_connection.md). Its relation to the general kernel-to-cokernel construction is explained in [the first quantum-normal connection](first_quantum_normal_connection.md). The derivative of the whole coefficients in (9), the moving-shift clock $t/N$, and the derivative of the central variable are all essential.

For $N>D$, every entry of $L_N,C_N,J_N$ is a Laurent polynomial in $U$ with exponents in $\{-1,0,1\}$. Indeed a term $Y^lS^k$ sends column $t$ to the residue of $t+l$, with the single carry $\lfloor(t+l)/N\rfloor$. The entries of $J_N$ have the same carries; differentiating coefficients or multiplying by $t/N$ does not change them. No estimate for a determinant or its inverse follows merely from this entrywise fact.

## 3. Fixed rank and bounded central degree

Let $r_N=\dim_{\mathbb C(U)}\ker L_N$. Then

\[
 1\le r_N\le w.
\tag{11}
\]

For the upper bound choose a generic complex value of $U$, a root $Y$ of $Y^N=U$, and evaluate a rational solution at its $N$ orbit points. The root equation is an order-$w$ cyclic recurrence. Its leading coefficient is nonzero at every orbit point for generic $U$, so its first $w$ values determine the remaining values successively. The residue-to-orbit evaluation matrix is invertible. The generic nullity of $L_N$ is therefore at most $w$. Nonzero $f_N$ gives the lower bound.

There is also a uniform degree bound for the large minors of this matrix. Let $I,J$ be row and column sets of size $N-r$, where $r\le w$. Expand a determinant term, and within each matrix entry choose one of its actual $Y$ shifts $l_t$. Its exponent of $U$ is

\[
 \frac{\sum_{t\in J}t-\sum_{s\in I}s+
                    \sum_{t\in J}l_t}{N}.
\tag{12}
\]

The first difference equals the difference of the omitted index sums, so its absolute value is at most $r(N-1)$. The last sum has absolute value at most $D(N-r)$. Consequently every such minor has Laurent support in $[-E,E]$, where one uniform choice is

\[
 E=D+w.
\tag{13}
\]

This bound survives cancellation and holds for all replacement minors used by Cramer's rule. It is not the much larger bound obtained by multiplying arbitrary entry degrees: the actual carry identity (12) is the reason the degree stays bounded.

Choose a nonzero maximal minor $\Delta_N$ of size $N-r_N$ with the smallest vanishing order at $U=1$ among all nonzero maximal minors. Reorder the selected rows and columns to write

\[
 L_N=\begin{pmatrix}A&B\\ \mathsf C&\mathsf D\end{pmatrix},
 \qquad \det A=\Delta_N.
\tag{14}
\]

The generic right and left kernel frames are

\[
 V_N=\begin{pmatrix}-A^{-1}B\\ I_r\end{pmatrix},
 \qquad W_N=\begin{pmatrix}-\mathsf C A^{-1}&I_r\end{pmatrix}.
\tag{15}
\]

Their entries are signed ratios of maximal minors, or constants. Every numerator therefore vanishes at least to the order of $\Delta_N$ at $1$. Cancelling that common power produces frames holomorphic at $U=1$, with common denominator $\widehat\Delta_N$ nonzero there. Numerators and denominator still have Laurent support in $[-E,E]$. The lower identity block in $V_N$ and right identity block in $W_N$ show that these are frames of the saturated generic kernel and its dual cokernel near $1$; this does not identify them with a possibly larger special-fiber kernel.

There is an additional, genuinely quantitative condition needed for reconstruction:

**Uniform frame condition.** After a common nonzero scalar normalization, the Laurent coefficients of $\widehat\Delta_N$ and of all the cancelled Cramer numerators in (15) are bounded, and $|\widehat\Delta_N(1)|$ is bounded below by a positive constant.

Since their degree is bounded, this gives a fixed disk $|U-1|<R_0$, $R_0<1/2$, on which the entries of $V_N,W_N$ and every fixed derivative are uniformly bounded. The estimate is entrywise; an $r\times N$ matrix with bounded entries need not have an operator norm bounded independently of $N$. Such a norm estimate is not used below. The frame condition is an explicit test on operator minors, not an assertion about the unknown selected solution. It is not automatic from nonzero minors at each level.

## 4. The unknown central coordinates have bounded Laurent degree

Let $T_N\subset\{0,\ldots,N-1\}$ be the $r_N$ free column indices in (15), and set

\[
 \mathbf a_N(U)=\frac N{K_N}\bigl(f_{t,N}(U)\bigr)_{t\in T_N}.
 \qquad
 \frac N{K_N}\mathbf f_N(U)=V_N(U)\mathbf a_N(U).
\tag{16}
\]

The indices $T_N$ may change with $N$. Every coordinate in the first formula remains an original residue coordinate from (3). Hence every coordinate of $\mathbf a_N$ has support in the same fixed carry interval $[k_-,k_+]$. No rational change of coordinates has been applied to these unknowns. It is the reconstruction matrix $V_N$, not the free coordinate vector, that is rational in $U$.

The complete and ordinary values determine the initial vector quantitatively. The inverse finite Fourier transform gives, for every $0\le t<N$,

\[
 f_{t,N}(1)=\frac1N\left[K_N+
       \sum_{j=1}^{N-1}C_j(q_N)Q_N^{-jt}\right].
\tag{17}
\]

Thus all coordinates of $\mathbf a_N(1)$ equal $1+o(1)$, uniformly even when their selected indices move with $N$. More precisely their errors have modulus at most $(N-1)D_N/|K_N|$. This is not an additional bound assumed on unknown normal jets.

Multiply the second equation in (10) by $W_N$ and substitute (16). The unknown first lift disappears because $W_NL_N=0$. The exact result is

\[
 B_N(U)U\mathbf a_N'(U)+E_N(U)\mathbf a_N(U)=0,
\tag{18}
\]

\[
 B_N=W_N C_N V_N,\qquad
 E_N=W_N\bigl(C_N U V_N'+J_N V_N\bigr).
\tag{19}
\]

Every coefficient here is constructed from (4), its first coefficient derivatives, root substitution, and minors. Neither $f_N$ nor its unknown first lift is needed to assemble (18). The state is used only to prove that its actual free coordinates solve it and to provide the already known data (17).

Let $\Delta$ denote the cancelled common denominator from Section 3. The entries of $B_N$ have denominator $\Delta^2$ and numerator support in $[-(2E+1),2E+1]$. The entries of $E_N$ have denominator $\Delta^3$ and numerator support in $[-(3E+1),3E+1]$. The latter assertion includes the derivative $UV_N'$: differentiating a Laurent numerator does not enlarge its support. Therefore multiplying (18) by $\Delta^3$ gives

\[
 \mathcal B_N(U)U\mathbf a_N'(U)+
            \mathcal E_N(U)\mathbf a_N(U)=0,
\tag{20}
\]

where both matrix Laurent bands lie in $[-L,L]$, with the fixed bound $L=3E+1$. Sums over $N$ entries can change their coefficients and conditioning, but do not change this degree bound.

## 5. A bounded matrix criterion using only fixed-degree identities

Put $d_c=k_+-k_-$ and write $\mathbf a_N(U)=U^{k_-}\mathbf b_N(U)$, where $\deg\mathbf b_N\le d_c$. Equation (20) becomes

\[
 \mathcal B_N U\mathbf b_N'+
          (k_-\mathcal B_N+\mathcal E_N)\mathbf b_N=0,
 \qquad \mathbf b_N(1)=\mathbf a_N(1).
\tag{21}
\]

Multiply the first equation by $U^L$ and equate coefficients. Together with evaluation at $1$, this is a linear system

\[
 H_N\mathbf x_N=(0,\mathbf a_N(1)),
\tag{22}
\]

where $\mathbf x_N$ is the vector of the $r_N(d_c+1)$ polynomial coefficients of $\mathbf b_N$. There are at most $r_N(d_c+2L+1)+r_N$ rows. Both dimensions are bounded independently of $N$. Redundant zero rows may be removed, and the homogeneous equation rows may be rescaled or combined by specified invertible row operations; their right side is zero. Such choices must be recorded when discussing conditioning.

**Finite matrix criterion.** Suppose the uniform frame condition holds and there is a choice of the just described operator-only row normalizations for which

\[
 \sigma_{\min}(H_N)\ge\delta>0
\tag{23}
\]

at all sufficiently large levels. Then the actual microscopic regular profiles are locally uniformly bounded near zero, with every fixed derivative bounded on smaller disks.

Indeed (17), (22), and (23) bound the coefficient vector $\mathbf x_N$ uniformly. The dimensions are bounded, so all choices of the usual finite-dimensional norms are uniformly equivalent. The fixed degree and fixed negative monomial in (21) bound $\mathbf a_N$ on $|U-1|<R_0$. Equation (16) and the uniform frame condition then give the exact scalar bound

\[
 g_N(z):=\frac{f_N(e^{z/N})}{K_N}
  =\frac1N\sum_{t=0}^{N-1}e^{tz/N}
       \bigl[V_N(e^z)\mathbf a_N(e^z)\bigr]_t=O(1)
\tag{24}
\]

on a fixed small $z$-disk. The factor $1/N$ cancels the number of residues; $|e^{tz/N}|\le e^{|z|}$ and $r_N\le w$.

For the [canonical ordinary interpolant and regular remainder](regularized_kashaev_period.md), denoted by $P_N^{\mathrm{ord}}$ and $R_N$, the [exact centered identity](scaled_meridian_regular_profile.md) is

\[
 g_N(z)=H_N^{\mathrm{res}}(z)\rho_N(z)+\pi_N(z),
 \quad H_N^{\mathrm{res}}(z)=\frac{\sinh(z/2)}{N\sinh(z/(2N))},
 \quad \rho_N(z)=e^{(N-1)z/(2N)}\frac{NR_N(e^{z/N})}{K_N}.
\tag{25}
\]

Here $\pi_N=P_N^{\mathrm{ord}}(e^{z/N})/K_N\to0$ with all fixed derivatives by (2). On a sufficiently small disk, $H_N^{\mathrm{res}}$ is uniformly nonzero. Thus (24) bounds $\rho_N$. Cauchy's inequality proves the derivative bounds. If a larger domain is controlled, the [boundary-circle division argument](scaled_meridian_regular_profile.md) applies across its resonance points; no larger domain is inferred from the local test.

A directly usable sufficient version of (23) is coefficientwise convergence of the normalized bounded matrices $H_N$ to a matrix $H_\infty$ with full column rank. One may use finitely many rank/chart subsequences, with the same uniform lower bound. This test concerns coefficients of a fixed-size algebraic system assembled from the actual source-normal operator. It does not assume convergence, boundedness, or a proposed value of the unknown profile.

At any one level, full column rank only gives algebraic uniqueness on the fixed carry range; its smallest singular value may still tend to zero. The distinction is precisely the remaining conditioning issue. The input degree bound alone does not imply (23).

## 6. A regular-singular alternative with finitely many resonance tests

There is another sufficient criterion when $B_N$ in (18) is generically invertible. Put $w_0=U-1$ and form the exact rational matrix

\[
 A_N(w_0)=-\frac{w_0}{U}B_N(U)^{-1}E_N(U),\qquad U=1+w_0.
\tag{26}
\]

The equation is $w_0\mathbf a_N'=A_N(w_0)\mathbf a_N$. Its rational degrees are bounded. For example the numerator and denominator of $B_N^{-1}E_N$ can be taken with Laurent half-width at most $(2r_N+1)E+r_N$, using the adjugate and the bounds following (19). Multiplication by $w_0/U$ changes this by at most two. This statement does not assert bounded coefficients or separation of the zeros of those denominators from $1$.

Assume the frame condition, and assume (26) is holomorphic on one fixed disk $|w_0|<R$, with $\|A_N\|\le C$ there. This is a concrete uniform Fuchsian test: after the indicated factor $w_0$ there is no pole, and the remaining fixed-degree denominators have a uniform zero-free disk. It can be established by cancelled coefficient bounds and a positive lower bound for their denominator values at zero. It is a test on the first-normal matrices, not an estimate of the unknown selected state.

Write $A_N(w_0)=\sum_{j\ge0}A_{j,N}w_0^j$. Choose an integer $J>2C$, and suppose

\[
 \sup_N\|(nI-A_{0,N})^{-1}\|<\infty
        \qquad (1\le n\le J).
\tag{27}
\]

For $n>J$, the Neumann series gives a uniform bound $2/n$ for the inverse. Hence a constant $C_1$ gives $\|(nI-A_{0,N})^{-1}\|\le C_1/(n+1)$ for every positive integer $n$.

The actual free coordinates are holomorphic at $U=1$. Their Taylor coefficients satisfy exactly

\[
 (nI-A_{0,N})\mathbf a_{n,N}
       =\sum_{j=1}^n A_{j,N}\mathbf a_{n-j,N},\qquad n\ge1.
\tag{28}
\]

Their constant coefficients are uniformly bounded by (17); the equation at order zero is automatically satisfied. On a slightly smaller fixed disk, Cauchy's estimate gives $\|A_{j,N}\|\le C_2 R_1^{-j}$. For $0<r<R_1$, multiply the norm of (28) by $r^n$, sum finite partial sums, and discard the helpful factor $1/(n+1)\le1$. If $t=r/R_1$ is small enough that $C_1C_2t/(1-t)<1/2$, the convolution term is absorbed. This proves

\[
 \sum_{n\ge0}\|\mathbf a_{n,N}\|r^n
       \le 2\sup_N\|\mathbf a_N(1)\|.
\tag{29}
\]

Equation (24) again proves local boundedness of $\rho_N$. If some positive integer residues are resonant or approach resonance, the same argument works after separately bounding the finitely many actual coefficients $\mathbf a_{n,N}$ for $0\le n\le J$. No extra jet bound is needed in the nonresonant case (27). The resonant version is a finite additional pointing requirement, not a claim that ordinary values already control those jets.

An especially simple operator-side test is $A_{0,N}\to A_0$ with no positive integer eigenvalue, together with the stated uniform Fuchsian bounds. Only finitely many inverses need checking because the residue norm is bounded. If the symbol $B_N$ is singular, this argument cannot be obtained by writing a formal inverse; the bounded matrix test in Section 5 remains meaningful without that inverse.

The [factorial atom and repeated-root diagnostic](source_corrected_quantum_normal_connection.md) illustrate the role of the source and resonance. For the actual factorial atom $(Y;Q)_N$, the supplied preoperator is $S-(1-Z_2Y)/(1-Y)$, with $Z_2=Q^N$. The residue calculation gives $U a'+U(1-U)^{-1}a=0$, whose root section is $a=1-U$. In (26) its residue is the positive integer $1$: its value at $U=1$ is zero and does not fix the first derivative. The resonance qualification is therefore necessary even for this elementary finite-source atom. For the previously recorded diagnostic $(S-1)(S-Z_2)$, the root operator is $(S-1)^2$ and both projected first-normal matrices vanish on its central solution line. The finite matrix in (22) then contains only the initial-value condition and cannot determine several allowed carries. These are checks of the supplied normal rule, not additional knot examples.

## 7. A conditional local meridian volume consequence

Either criterion proves more than an abstract normal-family statement when combined with the complete scalar theorem. The original subtraction gives

\[
 \rho_N(0)=\frac{K_N-P_N^{\mathrm{ord}}(1)}{K_N}=1+o(1).
\tag{30}
\]

Suppose one of Sections 5–6 bounds $|\rho_N|$ by $C$ on $|z|<R$. Cauchy's inequality bounds its first derivative by $2C/R$ on $|z|\le R/2$. For all sufficiently large $N$, (30) differs from $1$ by at most $1/4$. Choose a fixed $r>0$ with $r\le R/2$ and $2Cr/R\le1/4$. Then

\[
 \frac12\le|\rho_N(z)|\le C\qquad (|z|\le r).
\tag{31}
\]

Shrink $r$ further if necessary so that the same disk has a fixed lower bound for $|H_N^{\mathrm{res}}|$. Since $\pi_N\to0$, (25) gives fixed positive lower and upper bounds for $|g_N|$ there as well. Consequently, if the complete scalar satisfies

\[
 \frac{2\pi}{N}\log|K_N|\longrightarrow V,
\tag{32}
\]

then uniformly for $|z|\le r$,

\[
 \frac{2\pi}{N}\log\bigl|R_N(e^{z/N})\bigr|\longrightarrow V,
 \qquad
 \frac{2\pi}{N}\log\bigl|f_N(e^{z/N})\bigr|\longrightarrow V.
\tag{33}
\]

For the first limit, use the exact factorization
$R_N(e^{z/N})=K_N N^{-1}e^{-(N-1)z/(2N)}\rho_N(z)$.
Its logarithm differs from $\log|K_N|$ by $-\log N+O(1)$ uniformly on the disk. For the second, $f_N(e^{z/N})=K_Ng_N(z)$ and the difference is $O(1)$. This proves both limits, including their uniformity, without assuming that $\rho_N$ converges to $1$ or even has a unique subsequential limit.

For a knot covered by the [strict-tree theorem](actual_conway_all_strict_tree_long_twist_volume.md) or its [net-twist formulation](actual_conway_net_twist_volume.md), the complete scalar theorem identifies $V$ with the volume of that same knot complement. The two conclusions in (33) then retain that geometric right side. They remain conditional on the explicit finite matrix or Fuchsian estimates above. The disk is fixed in $z$, hence has meridian radius $O(1/N)$; this does not contradict the [nearby-zero theorem](actual_ado_complete_meridian_zero_accumulation.md) or give a zero-free neighborhood of fixed radius in $M$. No extension to all microscopic disks or identification of a selected classical factor is inferred.

## 8. The remaining conditioning problem

The actual finite source already supplies (1)–(5), the fixed carry interval, and the ordinary initial estimate (17) for a knot with the proved positive scalar rate. The whole preoperator is obtained from its finite summation rules, not from a fit to invariant values. From that supplied preoperator, Sections 2–4 prove the exact normal matrix equation and the bounded central degrees without a profile hypothesis. Sections 5–6 prove two quantitative sufficient criteria, and Section 7 gives their conditional local meridian volume consequence.

What is not supplied by the scalar theorem is the uniform frame condition, a lower singular-value bound for (22), or the alternative Fuchsian and residue estimates. Those are operator/lattice conditioning statements. They can now be phrased using bounded central degrees and a fixed number of free coefficients; their validity for a broad knot class remains open. The matrix test avoids an unspecified infinite family of normal-derivative estimates, but does not prove its own lower bound.

The separate [quarter-turn comparison](actual_main_meridian_turn_comparison.md) establishes a polynomial spectral estimate for each physical tangle turn on a small fixed meridian-displacement disk, relative to the complete turn of the same polynomial. This is a bound for a local tensor operation. It does not give a lower bound for the minors defining the reconstruction frame or for the smallest singular value in (22), and it does not establish the Fuchsian criterion. The conditioning hypotheses of this note are therefore unchanged. The [whole-source growth theorem](actual_main_meridian_source_bounds.md) goes further for strict trees with separated bare product junctions: it proves an exact supremum-volume limit, at both parities, for the unsummed auxiliary-colored source on \(|s|\le R<1\). Its uniform upper bound uses the augmented volume, and its lower witness is the complete point. That statement does not supply uniform conditioning of this finite system, local boundedness of the normalized filled-knot remainder, or the pointwise conclusion in Section 7. Thus these operator hypotheses remain genuine additional conditions.

The use of $f_N$ rather than the affine remainder does not discard the latter's source. The identity $f_N=S_NR_N+P_N^{\mathrm{ord}}$ is retained throughout, the ordinary values determine (17), and (25) uses the same actual subtraction and full-state centering monomial. If one writes a root equation directly for $R_N$, conjugation by $S_N$ produces the inhomogeneous term from $P_N^{\mathrm{ord}}$; it cannot be set to zero. Likewise, any boundary factor already present in the specified whole preoperator remains inside $L_N$ and its full generic kernel. No rank-one quotient is silently taken.

Finally, the [central comparison](central_source_freedom_in_regular_profiles.md) $\widetilde f_N=h_N(Y^N)f_N$ preserves the root equation, ordinary values, affine root source and Mellin quantum jets. It does not generally satisfy (10) for this same whole preoperator. Conversely, even a uniqueness result for (18) at each level would not imply the uniform estimates in Sections 5–6. The new test separates these two issues explicitly. It proves no identification of a classical geometric factor, no fixed meridian neighborhood free of zeros, and no particular limit such as $\rho_N\to1$.

## 9. Relation to established difference-equation constructions

Additional differential data at a root of unity have an established role in difference equations. Hardouin's *Iterative q-Difference Galois Theory*, Section 3.2, descends iterative data to a fixed subspace and gives a connection there; this is related to the need to retain more than the root shift alone. Di Vizio and Hardouin study the cyclic iterate and root specializations in their treatment of generic Galois groups. These results do not provide the uniform frame or conditioning bounds assumed here. [Hardouin's primary preprint](https://arxiv.org/pdf/0910.4826), [Di Vizio–Hardouin's author text](https://divizio.perso.math.cnrs.fr/PREPRINTS/qGKGENERIC-gros/qGKgeneric.pdf).

Central variables also compress degree bounds in the reduced-norm computation of Bostan, Caruso and Schost, Section 3. Their setting is positive-characteristic differential and shift operators. The present carry calculation is given explicitly in (12), and the source-normal and quantitative estimates are proved here with their stated hypotheses; no identification with that different setting is required. [Bostan–Caruso–Schost's primary preprint](https://arxiv.org/pdf/1405.5341).
