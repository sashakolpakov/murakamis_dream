# Exact period monodromy of the unturned endpoint recurrence

Private written proof, 16 November 2026.

The ordinary unturned recurrence has an explicit two-dimensional
monodromy over one full angular period. Its trace follows from the
entire characteristic polynomial of a generic cyclic orbit, including
the repeated physical eigenvalues. This supplies branch data for a
possible homogeneous scalar continuation. It does not choose that
continuation's actual source coefficients or bound them.

## 1. Ordinary recurrence and generic orbit

Put
\[
 N\ge2,\quad h=N^{-1},\quad \theta=\pi/N,\quad
 s_r=2\sin(r\theta),\quad c_r=2\cos((2r+1)\theta),
\]
\[
 c_N(x)=2\cos(2\pi x+\pi h),\qquad
 P_N(w)=2T_N(w/2)+2=\prod_{j=0}^{N-1}(w-c_j).
 \tag{1}
\]
The original ordinary difference operator is
\[
 \mathscr J_NF=(c_0+A_N+B_N)F-A_NF(x+h)-B_NF(x-h),
\]
\[
 A_N(x)=\frac{s_{Nx+1}^{\,4}}{s_{2Nx+1}s_{2Nx+2}},
 \qquad
 B_N(x)=\frac{s_{Nx}^{\,4}}{s_{2Nx}s_{2Nx+1}}.
 \tag{2}
\]
These are meromorphic coefficient functions of \(x\), of period
one. This is the ordinary operator, not a relation imposed only
after canonical reduction.

Initially fix \(x\) with
\[
                         2Nx\notin\mathbb Z.                \tag{3}
\]
Then every coefficient on the orbit \(x+lh\), \(l\in\mathbb Z\),
is finite, and \(A_N,B_N\) there are nonzero. The \(N\) spectral
points \(c_N(x+lh)\), \(0\le l<N\), are distinct. Indeed, equality
of two cosine values would imply either equality of their indices
modulo \(N\), or \(2Nx+l+k+1\in N\mathbb Z\), excluded by (3).

For a scalar solution of \((\mathscr J_N-w)F=0\), use the state
\[
 Y_F(x)=\binom{F(x)}{F(x-h)},\qquad
 Y_F(x+h)=T_N(x,w)Y_F(x),
\]
\[
 T_N(x,w)=
 \begin{pmatrix}
 (c_0+A_N(x)+B_N(x)-w)/A_N(x)&-B_N(x)/A_N(x)\\
 1&0
 \end{pmatrix}.
 \tag{4}
\]
Its period transfer is the ordered product
\[
 M_N(x,w)=T_N(x+(N-1)h,w)\cdots T_N(x,w).                    \tag{5}
\]
In particular no inverse-period or opposite-power convention enters
this definition.

## 2. The full twisted cyclic determinant

Write \(A_l=A_N(x+lh)\), \(B_l=B_N(x+lh)\), and
\[
                    a_N(x)=(-1)^N\prod_{l=0}^{N-1}A_l.
 \tag{6}
\]
The sine products give the exact identities
\[
 \prod_{l=0}^{N-1}\frac{B_l}{A_l}=1,\qquad
                  a_N(x)=\tan^2(\pi Nx).                    \tag{7}
\]
For the first, the fourth powers in
\(B_l/A_l=s_{Nx+l}^4s_{2Nx+2l+2}/
 [s_{Nx+l+1}^4s_{2Nx+2l}]\) telescope over a period.
For the second, put \(\rho=Nx\). The numerator of the product
of the \(A_l\) is \(16\sin^4(\pi\rho)\). Its denominator is
\[
 \prod_{m=1}^{2N}s_{2\rho+m}
       =(-1)^N\left(\prod_{m=1}^Ns_{2\rho+m}\right)^2
       =(-1)^N\,4\sin^2(2\pi\rho).
 \tag{8}
\]
Here \(\prod_{m=1}^N2\sin((z+m)\pi/N)=2\sin(\pi(z+1))\)
was used before squaring. Equations (6)--(8) prove (7) at
both parities.

For \(\mu\ne0\), let \(J_\mu(x)\) be the \(N\)-dimensional
cyclic operator (2), with the boundary convention
\[
                     F_{l+N}=\mu F_l.                      \tag{9}
\]
Thus the forward term in row \(N-1\) carries \(\mu\), and
the backward term in row zero carries \(\mu^{-1}\).

**Lemma.** For every \(N\ge2\), on the generic set (3),
\[
 \boxed{\quad
 \det(wI-J_\mu(x))
       =P_N(w)+a_N(x)(2-\mu-\mu^{-1}).
 \quad}                                                     \tag{10}
\]

*Proof.* First take \(\mu=1\). The original Newton polynomials
\[
 e_k(C)=\frac{\prod_{r<k}(c_r-C)}
                    {\prod_{r=1}^k s_r^2},\qquad 0\le k<N,
\]
form a basis of the polynomials of degree less than \(N\).
The ordinary source identity gives
\[
 \mathscr J_N[e_k(c_N(x))]
      =c_k e_k(c_N(x))-s_k^2e_{k-1}(c_N(x)),                 \tag{11}
\]
where the last term is zero at \(k=0\).
Evaluation on the \(N\) distinct points in section 1 is invertible.
Since these evaluated polynomials are period one in \(x\),
it conjugates \(J_1(x)\) to the triangular matrix in (11).
Consequently
\[
                         \det(wI-J_1(x))=P_N(w).            \tag{12}
\]
This is a characteristic-polynomial identity. In particular every
double eigenvalue and the odd simple eigenvalue has its original
multiplicity; vanishing at the distinct physical roots alone would
not prove (12).

For \(N\ge3\), the determinant expansion has only two terms with
uncanceled winding across the cyclic boundary. The all-forward
permutation contributes
\((-1)^{N-1}\mu\prod_lA_l=-a_N\mu\), and the all-backward
permutation contributes \(-a_N\mu^{-1}\), using (7).
Every other permutation has winding zero, so its boundary factors
cancel. This follows also by decomposing a permutation into cycles:
a nearest-neighbor cycle with nonzero winding must traverse all
\(N\) vertices. Comparing with \(\mu=1\) proves (10).

At \(N=2\), the two shifted neighbors occupy the same matrix entry.
The off-diagonal entries of \(wI-J_\mu\) are
\[
                 A_0+B_0\mu^{-1},\qquad B_1+A_1\mu.
\]
Their product has the \(\mu\)-dependent part
\(A_0A_1\mu+B_0B_1\mu^{-1}\).
Since \(a_N=A_0A_1=B_0B_1\), subtracting its value at
\(\mu=1\) again gives (10). \(\square\)

## 3. Exact monodromy and its branch information

**Theorem.** For every \(N\ge2\), the period transfer satisfies
\[
 \boxed{\qquad
 \det M_N(x,w)=1,\qquad
 \operatorname{tr}M_N(x,w)
       =2+P_N(w)\cot^2(\pi Nx).
 \qquad}                                                    \tag{13}
\]
The assertion initially holds under (3) and then as a meromorphic
identity in \(x,w\).

*Proof.* The determinant in (4) is \(B_N/A_N\), so (7) gives
the first assertion. A nonzero state with period multiplier
\(\mu\) exists exactly when either \(M_N-\mu I\) or
\(wI-J_\mu\) is singular: the recurrence and the two boundary
conditions (9) identify their kernels.
Multiplying (10) by \(\mu\) gives
\[
 \mu\det(wI-J_\mu)
 =-a_N\left[
   \mu^2-\left(2+\frac{P_N(w)}{a_N}\right)\mu+1\right].
 \tag{14}
\]
For generic \(w\), this quadratic has distinct roots; they are
the two roots of the monic characteristic polynomial of \(M_N\).
The two monic quadratics therefore agree. Polynomial continuation
in \(w\) includes the repeated-root cases, and (7) gives (13).
All quantities are meromorphic, which gives the stated continuation
in \(x\). \(\square\)

If a homogeneous scalar is continued so that its recurrence and
all the required shifted values are defined, Cayley--Hamilton gives
\[
 \boxed{\quad
 F(x+1)+F(x-1)
   =\{2+P_N(w)\cot^2(\pi Nx)\}F(x).
 \quad}                                                     \tag{15}
\]
Indeed \(Y_F(x+1)=M_N(x,w)Y_F(x)\), and period one of the
coefficients gives \(Y_F(x-1)=M_N(x,w)^{-1}Y_F(x)\).
Equation (15) is not an assertion that a function originally given
on a smaller rectangle already has such a continuation.

For the actual microscopic parameter \(w=2\cosh(\alpha/N)\),
\[
                         P_N(w)=4\cosh^2(\alpha/2).         \tag{16}
\]
On either horizontal line \(|\operatorname{Im}x|=H>0\),
uniformly in \(\operatorname{Re}x\) and bounded complex \(\alpha\),
\[
 \operatorname{tr}M_N(x,w)
          =-2\cosh\alpha+O_H(e^{-2\pi NH}).                  \tag{17}
\]
Thus its two multipliers tend, as an unordered pair with
multiplicity, to \(-e^\alpha,-e^{-\alpha}\).
On parameter sets avoiding their collisions, individual locally
labeled multipliers have the same exponential error as (17).
At a collision only the multiset convergence is asserted here.

There is also an exact elementary obstruction to an overly
restrictive choice of continuation. If \(P_N(w)\ne0\), a solution
which is period one in \(x\) on a full generic orbit must vanish:
(15) would give \(P_N(w)\cot^2(\pi Nx)F(x)=0\).
Equivalently \(J_1(x)-w\) is invertible by (12).
Consequently a nonzero homogeneous continuation cannot be a
globally single-valued function of \(e^{2\pi ix}\) extending
regularly around that whole orbit. A local branch on a buffered
half-strip is not excluded. The same distinction applies to a
proposed root-of-unity hypergeometric or factorial formula.

At \(P_N(w)=0\), the trace in (13) is exactly two.
This does not imply that \(M_N=I\); a nontrivial Jordan part
may remain. The actual matrix and its Jordan data must be retained;
the trace identity does not justify a semisimple replacement.

## 4. Actual source and remaining estimate

The ordinary full kernel is not a homogeneous solution at generic
microscopic \(w\). The pinned original source gives
\[
 (w-\mathscr J_N)K_N(c_N(x),w)
     =\frac{\eta P_N(w)}{N^2}e_{N-1}(c_N(x))
     =\frac{P_N(w)P_N(c_N(x))}
                    {N^4(c_N(x)-c_0)},\qquad \eta=(-1)^{N-1}.
 \tag{18}
\]
The removable interpretation in (18) is the original polynomial
one. On a physical bulk window the right side and its first
normal vanish, but it cannot be deleted off that grid.

The sharp Green budget in the second pinned source retains both
the baseline's ordinary defect and its actual right boundary
packet on every fractional grid. Equation (13) fixes a necessary
period-transfer invariant of any exact homogeneous replacement.
It does not determine which linear combination or periodic
coefficient functions match the kernel's physical jets.
Nor does it bound such coefficients on a tall rectangle, establish
the sharp \(J_\delta\) comparison, or estimate the complementary
original currents. No actual source coefficient, nonvanishing
term, or filled-action estimate is inferred from (13)--(17).

## 5. Coverage and complete direct sources

The ordinary Askey--Wilson recurrence, its polynomial triangular
action, and the retained full-kernel forcing are prior results.
The additional calculation here is its exact twisted cyclic
determinant and full-period transfer trace, with both parity
multiplicities and the \(N=2\) case retained.

The following complete source texts were read at the pinned
versions, and every directly used implication was checked:

* [Original ordinary recurrence and kernel source](research_edge_kernel_difference_and_endpoint_bound.md),
  SHA256 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da.
* [Sharp truncation forcing and retained Green boundary packet](research_partial_endpoint_green_boundary_budget.md),
  SHA256 a1bbfaa8f64abca96d2b97078a9d87fbc60877b4f4791612b1e8e2d822be286e.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Frozen notes and public manuscripts are
unchanged.
