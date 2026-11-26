# The exact ordinary-color transform from terminal type three to four

Research deduction, 5 November 2026. The completed type-three terminal
polynomial determines the type-four polynomial by a specific linear
operation on its ordinary color. That operation is a turn, crossing
multiplication, and turn in the full Hermite algebra. It also has an
exact contour representation retaining every physical first normal.
The new type-three local packet does not yet estimate this contour.

Use the original conventions
\[
 q=e^{\pi i/N},\quad r=q^{-2},\quad D=N-1,\quad
 \kappa=q^{D^2/2},\quad P_j=(r;r)_j,
 \qquad N\ge2.
 \tag{1}
\]
Let \(e_j(w)\), \(v(w)=(e_0(w),\ldots,e_D(w))^T\),
\(M\), and \(J\) be the original Newton basis, evaluation
vector, crossing multiplication matrix, and coefficient reversal.
Write \(\mathsf T f\) for reversal of the Newton coefficients
of a polynomial \(f\) of degree less than \(N\), and
\(\mathsf R f\) for the canonical representative of its product
with the original crossing in the full quotient algebra. Thus their
coefficient matrices are \(J\) and \(M\), respectively, and
\(M^T=JMJ\). These conventions are those of
[the exact contraction](research_mixed_wire_exact_contraction.md)
and [the original source interface](research_three_four_source_interface.md).

## 1. An identity of the entire ordinary-color polynomial

For each \(X\ne0\), write
\[
 \mathcal V_{0,N}(w,X)=v(w)^T a_N(X).
 \tag{2}
\]
Then, at both level parities and for every ordinary color,
\[
 \boxed{\quad
 \mathcal V_{1,N}(w,X)
 =\frac1{\kappa N}v(w)^TM^Ta_N(X)
 =\frac1{\kappa N}
       (\mathsf T\mathsf R\mathsf T\,
                        \mathcal V_{0,N}(\,\cdot\,,X))(w).
 \quad}
 \tag{3}
\]
To prove this first at \(X=r^b\), use the exact formulas from
[Gram transport, equation (2)](research_mixed_terminal_gram_shift.md):
\[
 \mathcal V_{\epsilon,N}(w,r^b)
 =\frac{(-q)^{-b}}{\kappa^{1+\epsilon}N^\epsilon}
                 (M^*M^{2+\epsilon}v(w))_b.
 \tag{4}
\]
The passage from \(\epsilon=0\) to \(1\) multiplies the
coefficient row on its right by \(M\), and adds the scalar
\((\kappa N)^{-1}\). Hence its coefficient column is multiplied
by \(M^T\), proving (3) at all \(N\) distinct physical nodes.
Both sides of (3) have outgoing Laurent band \([-D,0]\).
Interpolation in \(X^{-1}\) proves the identity for every
\(X\ne0\). It is a polynomial identity in \(w\), so every
ordinary derivative is retained without dividing by a Newton value.

This operation recovers the already known reversed-cap sum exactly.
Indeed the
[type-three Newton reduction](research_mixed_terminal_three_newton_reduction.md)
gives
\[
 a_{N,l}(X)=\frac{N(-q)^{-l}}{P_l}C_{1,N}(X,r^l),
 \qquad
 M_{lj}=\kappa(-1)^lq^{l+j^2}{l\brack j}_{q^2}.
 \tag{5}
\]
The \((-q)^{-l}\) factor cancels the row factor of \(M\).
Since \(b(w)=Sv(w)\) and
\(S_{lj}=\kappa^{-1}(-q)^{-l}M_{lj}/P_l\),
\[
 \sum_{j=0}^l q^{j^2}{l\brack j}_{q^2}e_j(w)
       =P_l b_l(w)=\mathcal H_N(w,r^{-l}).
 \tag{6}
\]
Consequently (3) is precisely
\[
 \mathcal V_{1,N}(w,X)
  =\sum_{l=0}^{D}\frac{C_{1,N}(X,r^l)}{P_l}
                           \mathcal H_N(w,r^{-l}),
 \tag{7}
\]
the whole source of
[reversed-cap assembly](research_mixed_reversed_cap_assembly.md).
Its conditional support \(i+l<N\), boundary phases, and ordinary
zeros have not changed. In particular (3) is not a type-three
binomial collapse of (7).

## 2. The full Hermite color contour

Use \(\mathscr P_N(z)=2T_N(z/2)+2\), where \(T_N\) is
the usual Chebyshev polynomial, so \(\mathscr P_N\) is monic
of degree \(N\). The original Frobenius functional is
\[
 \phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{\mathscr P_N}f,
 \qquad \phi_N(e_i e_j)=J_{ij}.
 \tag{8}
\]
Define the known polynomial kernel
\[
                 \mathscr K_N(z,w)=v(z)^TJMv(w).
 \tag{9}
\]
For any positively oriented contour \(\Gamma\) enclosing all
zeros of \(\mathscr P_N\), (3) gives the exact formula
\[
 \boxed{\quad
 \mathcal V_{1,N}(w,X)
 =\frac{(-1)^D N}{\kappa}\frac1{2\pi i}
    \oint_\Gamma
       \frac{\mathcal V_{0,N}(z,X)\mathscr K_N(z,w)}
            {\mathscr P_N(z)}\,dz .
 \quad}
 \tag{10}
\]
Indeed \(\phi_N(\mathcal V_{0,N}(z,X)\mathscr K_N(z,w))
=a_N(X)^TMv(w)\) by (8). For any polynomial \(f\),
division by the monic \(\mathscr P_N\) and the coefficient
of \(z^{-1}\) at infinity show
\[
 \frac1{2\pi i}\oint_\Gamma\frac{f(z)}{\mathscr P_N(z)}\,dz
             =[z^D]\operatorname{rem}_{\mathscr P_N}f.
 \tag{11}
\]
Combining these identities proves (10) with its displayed scalar.
The contour includes the simple complete node at odd levels and all
double nodes. At even levels the complete color \(-2\) is off
the physical grid; (10) still evaluates its original polynomial.
Residues at double nodes include the first derivatives of the entire
numerator. Thus no value-only quotient, omitted normal, or even-level
off-grid replacement is implicit in this formula.

## 3. The estimate still needed

The [complete type-three theorem](research_mixed_terminal_three_full_completion.md)
proves a nonzero packet on a fixed ordinary-color neighborhood of
\(-2\), with fixed jets and an outgoing plateau upper plane.
It supplies no estimate for (10) after discarding the rest of its
physical-node contour. Such a deformation would have to control the
off-complete-color part of the integrand, its actual kernel phases,
and every enclosed first normal. A norm or Cauchy estimate alone
does not identify a nonzero observed coefficient.

The known crossing-preservation theorem concerns \(\mathsf R\),
whereas (3) contains \(\mathsf T\mathsf R\mathsf T\).
[Unrestricted preservation under a turn is false](research_boundary_crossing_packet_preservation.md#7-why-unrestricted-closure-under-turns-is-false).
At odd levels the physical identity
\(v(-2)^TM=\varrho_N v(-2)^T\) is a left-eigenvector identity;
it does not replace the right vector \(Mv(-2)\) in (4) by a
scalar multiple of \(v(-2)\).

Thus (10) specifies an exact alternative observation problem for
the newly proved source, while (7) remains the direct coherent source
for type four. No type-four supporting plane, noncancellation,
ordinary closure, or arbitrary short-filling conclusion is obtained
by this algebraic deduction. No numerical computation is required.
