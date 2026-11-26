# When factorial zeros permit a rectangular index domain

A finite sum supported on a polytope can sometimes be extended to a complete index box because its exact summand vanishes at the added grid points. The adjacent pair has this property. It is not a general property of Newton gate formulas: distinct zero and pole hyperplanes need not cancel at their intersections.

This note gives the exact local criterion, a class of arbitrary-dimensional capacity sums for which it holds automatically, and an obstruction in the original Newton multiplication coefficient. It concerns the specified canonical interpolation. Equal values on a finite grid alone do not determine its divisors or its boundary behavior.

## 1. The divisor of a canonical factorial

For the canonical \(G_N\), the finite logarithmic derivative is
\[
 \frac{G_N'(z)}{G_N(z)}
 =\frac{\pi}{N^2}\sum_{k=0}^{N-1}(z-k)
                      \cot\frac{\pi(z-k)}N.        \tag{1}
\]
At an integer \(n=k+qN\), \(0\le k<N\), the residue of (1) is \(q\). At \(q=0\) its apparent singularity is removable. Thus
\[
                    \operatorname{ord}_{z=n}G_N(z)
                       =\left\lfloor\frac nN\right\rfloor.     \tag{2}
\]
In particular \(G_N\) is holomorphic on \(\Re z>-1\), has no zeros on \(\Re z<N\), and its only poles or zeros in the plane are at integers. These assertions also follow by continuing the original nonzero strip with its sine recurrence. Positive order means a zero and negative order means a pole.

Consider a fixed factorial expression
\[
 F_N(\mathbf z)=U_N(\mathbf z)
                 \prod_{j=1}^{s}G_N(\ell_j(\mathbf z))^{\nu_j}, \tag{3}
\]
where \(\ell_j(\mathbf z)=\mathbf a_j\cdot\mathbf z+c_j\) is a nonconstant integral affine form, \(\nu_j\in\mathbb Z\), and \(U_N\) is holomorphic and nonzero near an integer grid point \(\mathbf k\). Constants and indices may depend on \(N\), but they are the actual ones in the source, not their large-\(N\) approximations.

Group together the proportional linear forms
\[
       \ell_j(\mathbf z)-\ell_j(\mathbf k)
                 =\mathbf a_j\cdot(\mathbf z-\mathbf k).
\]
For a group corresponding to a hyperplane \(H\), set
\[
 q_H(\mathbf k)=
 \sum_{j:\,\ker\mathbf a_j=H}
          \nu_j\left\lfloor\frac{\ell_j(\mathbf k)}N\right\rfloor.
                                                               \tag{4}
\]

**Theorem 1.** Expression (3) is holomorphic near \(\mathbf k\) if and only if every \(q_H(\mathbf k)\ge0\). If it is holomorphic, its value at \(\mathbf k\) is zero if and only if at least one \(q_H(\mathbf k)>0\).

**Proof.** Equation (2) factors each composed factorial into a holomorphic unit and the indicated linear form raised to its integer order. Proportional linear forms differ only by a nonzero constant. The product therefore has local form
\[
                U_N^*(\mathbf z)\prod_H L_H(\mathbf z-\mathbf k)^{q_H},
\]
with \(U_N^*\) a holomorphic unit and distinct irreducible linear factors \(L_H\). A negative exponent leaves a pole along that hyperplane; zeros along other hyperplanes cannot remove it. If all exponents are nonnegative, the product is holomorphic, and its value is zero precisely when at least one exponent is positive. \(\square\)

The sum of all orders is not a substitute for (4). A positive total order can coexist with an uncancelled pole divisor.

## 2. A capacity class with arbitrary dimension

Fix nonzero vectors \(\mathbf a_e\in\mathbb Z_{\ge0}^m\), integers \(b_{e,N}\ge0\), and positive integers \(\nu_e\). Let \(p_v\ge0\). Consider
\[
 F_N(\mathbf k)=
 A_N(\mathbf k)
 \frac{\prod_e G_N(\mathbf a_e\cdot\mathbf k+b_{e,N})^{\nu_e}}
      {\prod_{v=1}^m G_N(k_v)^{p_v}},
 \qquad 0\le k_v<N,                               \tag{5}
\]
where the prefactor is regular at these grid points. Define the capacity polytope
\[
 {\cal P}_N=\{\mathbf k\in\{0,\ldots,N-1\}^m:
           \mathbf a_e\cdot\mathbf k+b_{e,N}<N
           \text{ for every }e\}.                 \tag{6}
\]

**Theorem 2.** The canonical expression (5) is holomorphic near every grid point in the box and vanishes at every point outside \({\cal P}_N\). Consequently
\[
                \sum_{\mathbf k\in{\cal P}_N}F_N(\mathbf k)
                 =\sum_{\mathbf k\in\{0,\ldots,N-1\}^m}F_N(\mathbf k).
                                                               \tag{7}
\]
This holds for any fixed finite list of capacities and every level.

**Proof.** All numerator arguments are nonnegative integers, so their orders (2) are nonnegative. Every denominator argument belongs to \(0,\ldots,N-1\), where \(G_N\) is nonzero. At a grid point violating a capacity, that numerator has positive order. Theorem 1 proves the assertions. \(\square\)

There is also a common pole-free complex product tube. Choose \(0<\theta_v<1\) with
\[
                  \sum_v a_{ev}\theta_v<1
                  \quad\hbox{for every }e.        \tag{8}
\]
Such a choice exists for any finite list. In normalized coordinates \(x_v=k_v/N\), use periods
\[
 -\theta_v/N\le\Re x_v\le1-\theta_v/N.
\]
The numerator factorials have real part greater than \(-1\), and the coordinate denominators have real part strictly between \(-1\) and \(N\). Thus the factorial part of (5) is holomorphic on their entire product, at arbitrary bounded imaginary heights. This avoids the corner poles that can occur if all left endpoints are fixed at the half-grid choice despite large row sums. Additional prefactors must still be checked on that tube.

## 3. An actual Newton gate that fails joint extension

The original multiplication coefficient is interpolated by
\[
 \mu_N(i,j,r)=
 \frac{G_N(i+j)G_N(r)}
      {G_N(i)G_N(j)G_N(r-i)G_N(r-j)G_N(i+j-r)}.     \tag{9}
\]
Its nonzero finite coefficients have
\(\max(i,j)\le r\le i+j<N\). It is tempting to extend all three variables simultaneously to the full box by factorial zeros. That is false for the canonical joint expression.

Take \(N=3\) and the grid point \((i,j,r)=(2,2,0)\). With increments \((u,v,w)\), formula (2) gives the local expression
\[
 \mu_3(2+u,2+v,w)
 =\text{holomorphic unit}\,
       \frac{(u+v)(w-u)(w-v)}{u+v-w}.              \tag{10}
\]
The denominator hyperplane is distinct from all three numerator hyperplanes. It therefore remains a genuine pole, even though the sum of the displayed orders is positive. This is an obstruction to the joint interpolation, not to the valid finite multiplication coefficient.

For fixed admissible inputs \(i,j\) with \(i+j<N\), varying only \(r\) is different: the forbidden output inequalities are enforced by reciprocal negative-factorial zeros, and the dangerous argument \(i+j-r\) never reaches \(N\). Sequential extensions may therefore work where a simultaneous extension fails. Their contours and changing parameter domains must be retained explicitly.

## 4. A balanced graph family

A useful member of the capacity class is associated to any finite loop-free graph \(\Gamma\). Parallel edges are allowed and are counted with multiplicity in every edge product, degree, and adjacency-matrix entry below:
\[
\begin{split}
 f_{\Gamma,N}(\mathbf x)
 ={}&\exp\left\{i\pi N\left(\sum_v x_v^2-\sum_{vw\in E}x_vx_w\right)
                    +i\pi(N-1)\sum_vx_v\right\}\\
 &\times
 \frac{\prod_{vw\in E}G_N(N(x_v+x_w))}
      {\prod_vG_N(Nx_v)^{\deg(v)+2}}.              \tag{11}
\end{split}
\]
Its grid support is \(k_v+k_w<N\) on every edge, so Theorem 2 gives a full rectangle. Each coordinate has quadratic balance and boundary order one: the quadratic matrix of its chirp is \(2I-\operatorname{Adj}(\Gamma)\), opposite to the sum of the factorial quadratic matrices; its residual linear coefficient is \(L_v=N-1\).

The exact multipliers under \(x_v\mapsto x_v+1\), writing \(w_v=e^{-2\pi ix_v}\), are
\[
 R_v(\mathbf w)=
 \frac{\prod_{u:\,uv\in E}(1-(w_uw_v)^N)}
                  {(1-w_v^N)^{\deg(v)+2}}.        \tag{12}
\]
Here is the joint normalization explicitly. Put \(Q=e^{2\pi i/N}\) and
\[
 \chi_N(w)=-\frac1N\sum_{k=0}^{N-1}k\Log(1-wQ^k)
                  +\frac{i}{2\pi N}\operatorname{Li}_2(w^N),
\]
\[
 \Phi_{\Gamma,N}(\mathbf w)=
 \sum_{uv\in E}\chi_N(w_uw_v)
       -\sum_v(\deg(v)+2)\chi_N(w_v).
\]
All branches are their convergent series at zero. If
\[
 c_N=\tfrac12\log N+i\pi(N/12-1/4+1/(12N)),\qquad
 C_{\Gamma,N}=e^{-(|E|+2|V|)c_N},
\]
then substitution of the exact factorial formula gives
\[
 \left(\prod_v w_v^N\right)f_{\Gamma,N}(\mathbf x)
       \exp\left(-\sum_vx_v\log R_v\right)
   =C_{\Gamma,N}\left(\prod_v w_v\right)e^{\Phi_{\Gamma,N}(\mathbf w)}.
                                                               \tag{14}
\]
The constants and exponents are fixed, not determined only up to a periodic function. The normalized product lower-kernel form is therefore
\[
 C_{\Gamma,N}e^{\Phi_{\Gamma,N}(\mathbf w)}
           \prod_v\frac{dw_v}{1-w_v^N},
\]
apart from the known factor \((-2\pi i)^{-|V|}\). It is holomorphic throughout every polydisk of radius less than one, and its integral over a complete product torus is zero.

Returning to the original kernel introduces the explicit factor
\(\exp(\sum_vx_v\log R_v)\). On a fixed small torus \(|w_v|=\rho\), its difference from one is \(O_\Gamma(\rho^N)\) on a bounded angular lift. Also
\[
 |\Phi_{\Gamma,N}|\le C_\Gamma N\rho/(1-\rho),\qquad
 |C_{\Gamma,N}|=N^{-(|E|+2|V|)/2}.
\]
Thus the original complete lower product integral is bounded by a fixed power of \(N\) times
\[
       \exp N\{C_\Gamma\rho/(1-\rho)+\log\rho+o(1)\}.
\]
For each prescribed rate, a sufficiently small fixed radius gives a strict bound below it. This is a theorem for complete product circles; partial faces still belong to the exact contour identity.

The side grouping is also exact in every dimension. If \(T_v\) translates \(x_v\) by one, then \(T_v f=R_v f\). Each \(R_v\) is unchanged by every integer translation. Hence, for every set \(J\) of side directions,
\[
       \prod_{v\in J}(T_v-1)f_{\Gamma,N}
          =f_{\Gamma,N}\prod_{v\in J}(R_v-1).       \tag{15}
\]
These are exactly the alternating side and corner differences in the tensor product of the one-variable residue identities on a full rectangle. For a left endpoint \(-\theta_v/N\), its side kernel is
\[
 -iN\,
 \frac{f(x_v+1,\widehat{\mathbf x})-f(x_v,\widehat{\mathbf x})}
      {1-e^{-2\pi i\theta_v}e^{-2\pi Ns}}\,ds,
 \qquad x_v=-\theta_v/N+is.
\]
The product kernels do not alter (15). This retains all mixed corners before taking absolute values; it does not assert that their rates are small.

This family is closed under joining two edge-disjoint graphs at specified vertices, provided the resulting graph remains loop-free and a shared vertex factor is divided out once:
\[
 F_{v,N}(x)=
 \frac{\exp\{i\pi Nx^2+i\pi(N-1)x\}}{G_N(Nx)^2}.   \tag{13}
\]
Indeed \(f_{\Gamma_1}f_{\Gamma_2}/\prod_{v\ {\rm shared}}F_{v,N}\)
is exactly (11) for the joined graph. The division removes the duplicated diagonal chirp and the duplicated two coordinate factorials. Without it, the boundary orders do not remain one.

Formula (11) is an explicit factorial class, not a claim about every branching knot source. The original degree-two power-two trace formulas produce the path members; the degree-three trace is a sum over an intermediate Newton output and does not obey the same single-factorial expression. For arbitrary compositions the [restored internal-wire theorem](research_internal_wire_exact_circle_averaging.md) is the broader actual source statement.

Neither rectangular extension nor positive boundary order supplies the geometric maximum or the needed bounds for all other contours. The proved gain is exact control of the index domain and of the algebraic boundary normalization, with the failure in (10) explicitly excluded.
