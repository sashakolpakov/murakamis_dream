# Boundary orders for balanced factorial integrands

Research note, 2 November 2026.

An exact factorial formula can turn an apparently dangerous end
of a summation contour into a removable singularity. The removal
is not automatic. This note gives an integer test for it, retains
all peripheral parameters in the required normalization, and
computes the residue when the test fails.

The statement applies to a single coordinate tending down the
imaginary direction while the other coordinates stay in a regular
parameter set. It makes no assertion about a geometric critical
point, a global contour deformation, or the survival of a saddle.

## 1. The factorial on both half-planes

Fix \(N\ge2\). Let \(G_N\) be the canonical sine factorial from
[the exact factorial calculation](research_exact_cyclotomic_factorial.md).
Set
\[
 Q=e^{2\pi i/N},\qquad
 c_N^\sigma=\frac12\log N+
   i\pi\sigma\left(\frac N{12}-\frac14+\frac1{12N}\right),
 \qquad \sigma\in\{1,-1\}.
 \tag{1}
\]
For \(\sigma\operatorname{Im}t<0\), put
\(\zeta=e^{-2\pi i\sigma t}\), so \(|\zeta|<1\). The exact formula is
\[
 \begin{split}
 \log G_N(Nt)={}&
    \frac{i\pi\sigma N}{2}t^2
    -\frac{i\pi\sigma(N-1)}2t+c_N^\sigma\\
 &+t\log(1-\zeta^N)
    -\frac1N\sum_{k=0}^{N-1}k\log(1-\zeta Q^{\sigma k})
    +\frac{i\sigma}{2\pi N}\operatorname{Li}_2(\zeta^N).
 \end{split}
 \tag{2}
\]
Every logarithm and dilogarithm on the second line is given by its
convergent series at zero. The formula for \(\sigma=1\) is the
lower-half-plane identity already proved from the Gamma product.
That product satisfies
\(G_N(\bar z)=\overline{G_N(z)}\); conjugation therefore proves
(2) for \(\sigma=-1\), including its constant.

There is also an exact way to remove a negative slope:
\[
 G_N(z)G_N(N-1-z)=N.
 \tag{2a}
\]
For a proof, the finite logarithmic derivative in the factorial
note is unchanged under \(z\mapsto N-1-z\), by replacing its
index \(k\) with \(N-1-k\) and using
\((-t)\cot(-t)=t\cot t\). The derivative of the logarithm
of the product in (2a) is therefore zero. At \(z=0\), the
product is \(G_N(N-1)=N\), by the elementary full sine
product. Meromorphic continuation proves (2a).

## 2. A general coordinate of a factorial source

Let \(\mathbf y\) denote the retained parameters. For each \(N\),
consider the exact integrand
\[
 \begin{split}
 f_N(x,\mathbf y)={}&A_N(\mathbf y)\,w^{d_N}
 U_N(w,\mathbf y)
 \exp\left(\frac{i\pi N\mathcal A}{2}x^2+2\pi iB_Nx\right)\\
 &\quad\times
 \prod_{j=1}^{s}
 G_N\!\left(N(a_jx+b_j)\right)^{\nu_j},
 \qquad w=e^{-2\pi ix}.
 \end{split}
 \tag{3}
\]
Here:

- \(a_j\) are nonzero integers, and \(\nu_j\) are integers;
  a negative multiplicity denotes a denominator factor.
- The shifts \(b_j=b_{j,N}(\mathbf y)\), the linear coefficient
  \(B_N=B_N(\mathbf y)\), and \(\mathcal A=\mathcal A(\mathbf y)\)
  are specified holomorphic functions on a connected parameter
  neighborhood.
- \(d_N\) is an integer. The factor \(U_N\) is holomorphic and
  nonzero on a disk about \(w=0\), with \(U_N(0,\mathbf y)=1\).
- \(A_N\) is holomorphic and nonzero on the parameter neighborhood.

Factors independent of \(x\) belong in \(A_N\). A nonzero
meromorphic prefactor in \(w\) can be put in this form by
extracting its integer order \(d_N\). The dependence of \(b_j\)
on \(N\) permits the original half-integer factorial shifts;
they are not rounded or removed.

Define
\[
 \sigma_j=\operatorname{sgn}a_j,\qquad m_j=|a_j|,\qquad
 r_j=e^{-2\pi i\sigma_j b_j},\qquad
 \zeta_j=r_jw^{m_j}.
 \tag{4}
\]
For sufficiently small \(|w|\), each \(|\zeta_j|<1\), and
\(a_jx+b_j\) lies in the half-plane required by (2).
Negative slopes thus cause no ambiguity: they use the upper
factorial formula, with its conjugated polynomial and constant.

Two combinations of the exact input data control the end:
\[
 \begin{split}
 \Delta&=\mathcal A+\sum_j\nu_j a_j|a_j|,\\
 L_N&=B_N+\frac N2\sum_j\nu_j|a_j|b_j
                    -\frac{N-1}{4}\sum_j\nu_j|a_j|,\\
 \kappa_N&=N-L_N+d_N.
 \end{split}
 \tag{5}
\]
The condition \(\Delta=0\) will be called quadratic balance.
It is an identity in the retained parameters, not a condition
checked only after setting them to their complete values.

Reflection (2a) replaces a factor with \(a_j=-m<0\) by
\[
 G_N(N(-mx+b_j))^{\nu_j}
  =N^{\nu_j}
   G_N\!\left(N\left(mx+\frac{N-1}{N}-b_j\right)\right)^{-\nu_j}.
 \tag{5a}
\]
This substitution leaves both \(\Delta\) and \(L_N\) unchanged.
For the latter assertion, its new contribution is
\[
 -\frac{N\nu_jm}{2}\left(\frac{N-1}{N}-b_j\right)
       +\frac{(N-1)\nu_jm}{4}
 =\frac{N\nu_jm b_j}{2}-\frac{(N-1)\nu_jm}{4}.
 \]
Thus the signed formula agrees exactly with reducing all slopes
to positive ones first. The displacement \((N-1)/N\) matters
in this check.

## 3. Exact descent and the integer order

**Theorem 1.** Suppose that \(\Delta=0\) and that
\(\kappa_N\) is an integer independent of \(\mathbf y\).
On a disk where all \(|\zeta_j|<1\), define
\[
 \begin{split}
 R_N(w,\mathbf y)
   &=\prod_j(1-\zeta_j^N)^{\nu_j a_j},\\
 \log R_N
   &=\sum_j\nu_j a_j\log(1-\zeta_j^N).
 \end{split}
 \tag{6}
\]
The logarithm is the one that vanishes at zero. Then
\[
 f_N(x+1,\mathbf y)=R_N(w,\mathbf y)f_N(x,\mathbf y).
 \tag{7}
\]
For the first lower lattice correction
\(h_N=e^{-2\pi iNx}f_N=w^Nf_N\), the function
\[
 H_N=h_N\,e^{-x\log R_N}
 \tag{8}
\]
descends to the punctured \(w\)-disk and has the exact expression
\[
 \boxed{
 H_N(w,\mathbf y)
   =C_N(\mathbf y)\,w^{\kappa_N}
            U_N(w,\mathbf y)e^{\Phi_N(w,\mathbf y)}.}
 \tag{9}
\]
The coefficient is nonzero and is completely specified by
\[
 C_N=A_N\exp\sum_j\nu_j
 \left[
    \frac{i\pi\sigma_jN}{2}b_j^2
   -\frac{i\pi\sigma_j(N-1)}2b_j+c_N^{\sigma_j}
 \right].
 \tag{10}
\]
The function \(\Phi_N\) is holomorphic and vanishes at zero:
\[
 \begin{split}
 \Phi_N=\sum_j\nu_j\bigg[
  b_j\log(1-\zeta_j^N)
   -\frac1N\sum_{k=0}^{N-1}k\log(1-\zeta_jQ^{\sigma_j k})
   +\frac{i\sigma_j}{2\pi N}\operatorname{Li}_2(\zeta_j^N)
 \bigg].
 \end{split}
 \tag{11}
\]

**Proof.** Substitute (2) into (3). The coefficient of
\(i\pi Nx^2/2\) is exactly \(\Delta\). The coefficient of
\(2\pi ix\) in the remaining polynomial is \(L_N\).
The constants are those in (10). The coefficient of \(x\) in
the nonpolynomial part is
\(\sum_j\nu_j a_j\log(1-\zeta_j^N)=\log R_N\);
the other terms are (11). Consequently
\[
 f_N=C_Nw^{d_N}U_N
             \exp(2\pi iL_Nx+x\log R_N+\Phi_N).
 \tag{12}
\]
Since \(a_j\) are integers, \(w\), every \(\zeta_j\), and
\(\Phi_N\) are unchanged by \(x\mapsto x+1\).
Also \(L_N=N+d_N-\kappa_N\) is an integer, so its exponential
has multiplier one. This proves (7). Multiplying (12) by
\(w^N\) and using (8) proves (9). Every term of (11) is
holomorphic and zero at zero. This proves all the assertions.
QED.

In particular, (6) retains the factors
\[
 1-e^{-2\pi i\sigma_jN b_j}w^{Nm_j}.
 \tag{13}
\]
Substituting \(b_j=0\) before forming (13) can change their
coincidences and cancellations. The peripheral parameters and
the half-integer shifts remain part of the exact formula.

## 4. The complete lower kernel and its residues

The sum of all lower geometric lattice modes is the exact kernel
\[
 \frac{f_N(x,\mathbf y)}{e^{2\pi iNx}-1}\,dx
   =-\frac1{2\pi i}
       \frac{h_N(x,\mathbf y)}{w(1-w^N)}\,dw.
 \tag{14}
\]
After the normalization (8), its one-form is
\[
 \Omega_N=
 -\frac{C_N}{2\pi i}\,
     w^{\kappa_N-1}
     \frac{U_N(w)e^{\Phi_N(w)}}{1-w^N}\,dw.
 \tag{15}
\]
The denominator is regular on any disk of radius less than one.

**Corollary 2.** On such a disk, \(\Omega_N\) is holomorphic at
zero if and only if \(\kappa_N\ge1\). More precisely:

- If \(\kappa_N\ge1\), the order of the form at zero is
  \(\kappa_N-1\).
- If \(\kappa_N=0\), it has a simple pole with nonzero residue
  \(-C_N/(2\pi i)\).
- If \(\kappa_N=-k<0\), it has a pole of order \(k+1\), and
  \[
   \operatorname{Res}_0\Omega_N
    =-\frac{C_N}{2\pi i}\,
       [w^k]\frac{U_N(w)e^{\Phi_N(w)}}{1-w^N}.
   \tag{16}
  \]

Here \([w^k]\) denotes the coefficient of \(w^k\). A higher
pole can have zero residue; the theorem does not confuse these
two properties.

**Proof.** The quotient after \(w^{\kappa_N-1}\) in (15) is
a holomorphic unit whose value at zero is one. This proves
the order statement and the coefficient formula. QED.

All higher lower modes have already been included in
\((1-w^N)^{-1}\). If one separates the \(r\)-th mode, \(r\ge1\),
its order in (9) is \(\kappa_N+(r-1)N\). Thus the test does
not omit a more singular member of that family.

If \(\kappa_N=p/q\) is rational but not integral, the same
calculation becomes single-valued on \(w=v^q\). The form then
has order \(p-1\) at \(v=0\). This is a statement on that
cover only; it does not establish descent of the original
form to the \(w\)-disk. A varying, nonrational peripheral
exponent cannot be removed by a fixed finite cover.

## 5. Returning to the original kernel

The exact kernel in (14) differs from (15) by
\(\exp(x\log R_N)\). Its removal is not an exact replacement
of the original source.

On a fixed parameter compact set and a circle \(|w|=\rho<1\),
suppose \(|\zeta_j|\le r<1\). Then
\[
 |\log R_N|
 \le \left(\sum_j|\nu_j a_j|\right)\frac{r^N}{1-r^N}.
 \tag{17}
\]
For the same circle,
\[
 |\Phi_N|\le
 \sum_j|\nu_j|
 \left[
   \left(|b_j|+\frac1{2\pi N}\right)\frac{r^N}{1-r^N}
   +\frac{N-1}{2}\frac{r}{1-r}
 \right].
 \tag{18}
\]
These follow by applying the convergent-series bounds to
(6) and (11); \(\sum_{k=0}^{N-1}k/N=(N-1)/2\).
On a lift of one full circle,
\[
 |e^{x\log R_N}-1|
       \le |x|\,|\log R_N|\,e^{|x||\log R_N|}.
 \tag{19}
\]
Here \(x=-\log w/(2\pi i)\) on a fixed bounded angular lift,
so \(|x|\) is bounded independently of \(N\) at fixed \(\rho\).

The estimates yield a useful conditional closure statement.

**Corollary 3.** Assume the finite lists \(a_j,\nu_j\) are
independent of \(N\), the \(b_j\) stay uniformly bounded,
and \(\kappa_N\ge1\) for every sufficiently large \(N\).
Suppose there are constants \(V_0,p,C,\rho_0>0\) such that
\[
 |C_N(\mathbf y)U_N(w,\mathbf y)|
       \le C N^p e^{NV_0}
 \quad (|w|\le\rho_0)
 \tag{20}
\]
uniformly on the retained parameter compact set.
For every prescribed real rate \(T\), a sufficiently small
fixed radius \(\rho>0\) makes the integral of the original
kernel (14), along the lift of a complete circle
\(|w|=\rho\), bounded by
\[
 C_T N^p e^{NT}
 \tag{21}
\]
for all sufficiently large \(N\).

**Proof.** The integral of \(\Omega_N\) on the complete
circle is zero by Corollary 2. Subtract it from the original
integral. Since \(\kappa_N\ge1\), the factor
\(\rho^{\kappa_N}\) obtained from (15) and the circle length
is at most one. The denominator \(1-w^N\) is bounded away
from zero.

The bounded shifts imply that a common bound
\(r(\rho)\ge\sup_{N,\mathbf y,j}|r_j|\rho^{m_j}\) tends to zero as
\(\rho\to0\). Equations (17)--(20) bound the exponential
rate of the difference by
\[
 V_0+\frac12\left(\sum_j|\nu_j|\right)
                \frac{r(\rho)}{1-r(\rho)}
        +\log r(\rho)+o(1).
 \tag{22}
\]
The bounded \(b_j\)-terms in (18) are exponentially small
at fixed \(\rho\), and the factors in (19) independent of
\(N\) are absorbed in the constant. Expression (22) tends
to \(-\infty\) as \(\rho\to0\). Choose it strictly below
\(T\); the resulting margin absorbs the \(o(1)\). QED.

The complete-circle qualification is essential. A partial
arc of (15) can have the full exponential size of \(C_N\).
This corollary neither supplies the missing part of that arc
in a global contour nor bounds currents in another retained
coordinate.

**Corollary 3a.** The conclusion also holds for a sum of at
most \(C N^q\) integrands of the form (3), provided the
hypotheses of Corollary 3 hold uniformly for every summand.
The summands need not have a common multiplier \(R_N\).

**Proof.** Choose the radius using the common bounds on
the signed multiplicities, slopes, shifts, and coefficients.
Apply Corollary 3 to each summand with a rate strictly
smaller than the prescribed one, and sum the bounds.
The extra polynomial number of terms is absorbed into
the strict exponential margin. The normalizations are
used separately inside these exact linear integral
identities; no common gauge is asserted. QED.

Thus a finite internal state sum can be treated term by
term if every retained term passes the same uniform order
test. That premise must include the exceptional terms
and any normal derivatives in the exact source.

## 6. The adjacent pair and a failure of automatic composition

For the \(x\)-coordinate in
[the adjacent-pair source](research_adjacent_pair_cyclotomic_gauge.md),
the \(x\)-dependent factorials are
\[
 G_N(N(x+y))\,G_N(Nx)^{-3}.
 \]
Thus
\[
 \mathcal A=2,\quad
 (a_1,a_2)=(1,1),\quad(\nu_1,\nu_2)=(1,-3),\quad
 (b_1,b_2)=(y,0),\quad
 B_N=\frac{N(1-y)-1}{2},\quad d_N=0.
 \]
Direct substitution gives
\[
 \Delta=0,\qquad L_N=N-1,\qquad\kappa_N=1,
 \]
and
\[
 R_N=\frac{1-(w e^{-2\pi iy})^N}{(1-w^N)^3}.
 \tag{23}
\]
Theorem 1 therefore recovers exactly the simple zero found
for that source, including its peripheral factor.

The same conclusion cannot be propagated merely by
multiplying two integrands. If two balanced integrands have
orders \(\kappa_N^{(1)}\) and \(\kappa_N^{(2)}\), their
product is balanced, but
\[
 \kappa_N^{(\mathrm{product})}
      =\kappa_N^{(1)}+\kappa_N^{(2)}-N.
 \tag{24}
\]
Only one first-mode factor \(w^N\) is supplied to the product.
Equation (24) follows directly from the additivity of
\(L_N\) and \(d_N\).

For a concrete factorial example, let
\[
 F_N(x)=
   \frac{\exp\{i\pi Nx^2+i\pi(N-1)x\}}{G_N(Nx)^2}.
 \tag{25}
\]
This has \(\Delta=0\) and \(\kappa_N=1\). Its normalized
complete lower kernel is holomorphic. The product \(F_N^2\)
has \(\kappa_N=2-N\). At \(N=2\), its normalized kernel has
a simple pole with nonzero residue.

This is not an even-level accident. At \(N=3\), the product
has \(\kappa_N=-1\). Its exponent (11) has linear coefficient
\[
 [w]\Phi_N=-\frac4N\sum_{k=0}^{N-1}kQ^k
                     =\frac4{1-Q}\ne0.
 \tag{26}
\]
Since \(U_N=1\), formula (16) gives a nonzero residue there
as well. Thus even within the class of balanced factorial
integrands, new poles and residues can appear under composition.
These examples concern algebraic integrands; they are not
counterexamples to any knot volume statement.

## 7. The chosen interpolation is essential

The lattice values and the shift multiplier do not determine
the boundary order. For an integer \(k\), the replacement
\[
 \widetilde f_N(x)=w^{kN}f_N(x)
 \tag{27}
\]
agrees with \(f_N\) at every point \(x=i/N\), where
\(w^N=1\). It also has exactly the same multiplier under
\(x\mapsto x+1\). Nevertheless its order is
\[
 \widetilde\kappa_N=\kappa_N+kN.
 \tag{28}
\]
For example, the interpolants \(1\) and \(w^{-N}\) give
identical lattice values and multiplier one, but their orders
are respectively \(N\) and zero. Their normalized lower
kernels are respectively regular and have a nonzero simple
pole.

Even the residue class of the order is not fixed by lattice
values and the multiplier alone. The polynomial
\[
 P_N(w)=w^N+(w^N-1)w
 \tag{29}
\]
equals one at every \(N\)-th root of unity and has a simple
zero at \(w=0\) for every \(N\ge2\). Multiplication by
\(P_N\) preserves the same finite data but increases
\(\kappa_N\) by one.

These observations do not authorize replacing the original
interpolation in a contour proof. Such replacements alter
the decomposition into lattice modes and can move contributions
to other parts of the contour. Theorem 1 concerns the exact
interpolant (3), including its chosen quadratic and linear
phases. Selecting that interpolant is additional information
beyond a recurrence or the finite lattice values.

## 8. What must be checked for another short filling

The exact summation formula determines the signed slopes,
multiplicities, shifts, and quadratic phase in (3). Equations
(5) then give a finite algebraic test at the chosen face.
If quadratic balance and the positive integer order hold,
Theorem 1 removes that boundary singularity after an explicit
normalization, and Corollary 3 controls a complete small
circle whenever (20) is available.

If the order is nonpositive, its residue is a concrete
lower-dimensional coefficient, given by (16), rather than
an error term that may be discarded. It may need to be
retained as another contribution. If quadratic balance
fails, the uncancelled Gaussian in \(x\), equivalently a
quadratic function of \(\log w\), is outside this theorem.
Neither defect can be repaired by setting the retained
peripheral parameters equal to one before performing the
calculation.

This provides a reusable test at a Newton face. It does not
yet provide closure of the class of all short-filling sources,
because (24) shows that the decisive order is not preserved
without additional input from the actual composition.

The standalone
[reproduction script](../experiments/check_balanced_factorial_boundary_order.py)
checks the translation multiplier by iterating the original sine
recurrence, separately from (6). It also checks (9) against the
unsimplified finite factorial formula. Its
[saved results](../repro/results/research-balanced-factorial-boundary-order.json)
cover both slope signs, slopes of magnitude greater than one,
half-integer shifts, both level parities, and positive, zero,
and negative orders at 80 decimal digits. These are numerical
diagnostics; the proofs are the exact identities above.
