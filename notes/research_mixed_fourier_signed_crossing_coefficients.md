# Signed crossing runs and their exact Fourier endpoint observation

Research deduction, 7 November 2026. The existing finite
\(q\)-binomial crossing factorization gives explicit coefficient
recurrences for every signed crossing run in the actual Fourier
basis. The first coefficient is a specified ordinary Hermite
observation of a terminal source. At physical incoming nodes it
is an original terminal-power vector followed by its Gram
observation, with the exact scalar retained.

This is a basis and observation dictionary for the original
source, not a new \(q\)-binomial technique or an asymptotic
preservation theorem. No numerical evaluation is used.

## 1. Both one-step coefficient recurrences

Fix \(N\ge2\), \(D=N-1\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad r=Q^{-1},\quad
 P_j=(r;r)_j,\quad F_j=(Q;Q)_j,\quad
 \kappa=q^{D^2/2},\quad \nu_j=(-1)^jq^{j(j+1)}.
 \tag{1}
\]
Let \(f_j\), \(\mathsf B\), and \(\mathsf\Gamma\) be the
original Fourier basis and operators in
[the closing interface](research_mixed_fourier_boundary_closing_interface.md),
Section 5. In particular,
\[
 \mathsf Bf_j=f_{j-1}\ (j\ge1),\quad \mathsf Bf_0=0,\qquad
 \mathsf\Gamma f_j=\kappa\nu_j f_j,\qquad
 \mathcal M_1=\mathscr P_N(\mathsf B)\mathsf\Gamma,\quad
 \mathscr P_N(\mathsf B)=\sum_{k=0}^{D}\frac{\mathsf B^k}{F_k}.
 \tag{2}
\]
This is the Fourier-basis form of
[terminal powers](research_terminal_powers_qbinomial.md),
Section 2. It includes the original endpoint projector in
\(\mathsf B=(Y^{-1}-\mathsf E^{-1})(I-\Pi_0)\).

For \(G=\sum_{l=0}^{D}c_l f_l\), write
\(\mathcal M_{\pm1}G=\sum_{m=0}^{D}c_m^\pm f_m\).
Then
\[
 \boxed{\begin{split}
 c_m^+&=\kappa\nu_m
      \sum_{k=0}^{D-m}\frac{r^{-mk}}{P_k}\,c_{m+k},\\
 c_m^-&=\kappa^{-1}\nu_m^{-1}
      \sum_{k=0}^{D-m}\frac{r^k}{P_k}\,c_{m+k}.
 \end{split}}
 \tag{3}
\]
There is no wrap at \(m+k=N\), and every denominator has
index below \(N\).

*Proof.* The original row action gives
\[
       \mathcal M_1f_l
             =\kappa\nu_l\sum_{m=0}^{l}\frac{f_m}{F_{l-m}}.
 \tag{4}
\]
For \(l=m+k\), the identity
\(\nu_{m+k}/F_k=\nu_m r^{-mk}/P_k\) proves the first
line of (3).

For the inverse, the finite \(q\)-binomial identity implies
\[
 \mathscr P_N(\mathsf B)^{-1}
     =\sum_{k=0}^{D}
       \frac{(-1)^kQ^{k(k-1)/2}}{F_k}\mathsf B^k
     =\sum_{k=0}^{D}\frac{r^k}{P_k}\mathsf B^k.
 \tag{5}
\]
Indeed, for \(1\le h<N\), the coefficient of
\(\mathsf B^h\) in the product of the first sum in (5)
with \(\mathscr P_N\) is
\[
 \frac1{F_h}\sum_{k=0}^{h}
       (-1)^kQ^{k(k-1)/2}{h\brack k}_Q
       =\frac{(1;Q)_h}{F_h}=0 .
 \tag{6}
\]
The constant coefficient is one and all terms of degree
at least \(N\) vanish because \(\mathsf B^N=0\).
The conversion in (5) uses
\(F_k=(-1)^kQ^{k(k+1)/2}P_k\).
Now \(\mathcal M_{-1}=\mathsf\Gamma^{-1}
\mathscr P_N(\mathsf B)^{-1}\); applying this in the stated
order proves the second line of (3). \(\square\)

In particular, both signed steps preserve the full band,
but neither step is a scalar multiplier on its first coefficient.

## 2. A finite chain sum with all support boundaries

For \(p\ge0\), define
\[
 \begin{split}
 L_+(m,l)&=\frac{\nu_m r^{-m(l-m)}}{P_{l-m}},\\
 L_-(m,l)&=\frac{\nu_m^{-1}r^{l-m}}{P_{l-m}},
                         \qquad 0\le m\le l<N .
 \end{split}
 \tag{7}
\]
Repeated application of (3) gives, for \(\sigma\in\{+1,-1\}\),
\[
 c_m^{(\sigma p)}
    =\kappa^{\sigma p}
       \sum_{m=j_0\le j_1\le\cdots\le j_p<N}
          \left(\prod_{h=1}^{p}L_\sigma(j_{h-1},j_h)\right)
                                    c_{j_p}.
 \tag{8}
\]
At \(p=0\) the single empty product returns \(c_m\).
All factors are complex original phases; (8) is not a
positive state sum.

For the actual cap, put
\[
 X=e^{-2\pi ia},\qquad
 c_l(X)=C_{1,N}(X,r^l),\qquad
 \rho_i(X)=X^{-i}(rX;r)_i.
 \tag{9}
\]
The original conditional polynomial has the exact physical
node expression
\[
 c_l(X)=\sum_{i=0}^{D-l}
          \frac{\rho_i(X)P_{i+l}}{P_i^3P_l}.
 \tag{10}
\]
Substitution into (8) therefore gives the complete finite sum
\[
 \boxed{\displaystyle
 c_m^{(\sigma p)}(X)
 =\kappa^{\sigma p}
  \sum_{\substack{m=j_0\le\cdots\le j_p<N\\0\le i<N-j_p}}
       \left(\prod_{h=1}^{p}L_\sigma(j_{h-1},j_h)\right)
       \frac{\rho_i(X)P_{i+j_p}}{P_i^3P_{j_p}} .}
 \tag{11}
\]
The nested order and final triangular wall in (11) are exact.
Terms beyond that wall vanish in the original finite product
at \(r^{j_p}\), before any interpolation.
No intermediate Fourier mode, ordinary normal, or crossing
scalar is removed. This formula does not license imposing
those physical zeros at an off-grid intermediate index.

## 3. The first coefficient as an original ordinary observation

Let
\[
 \mathcal A_{n,N}(X)
    =[f_0]\,\mathcal M_n Z_N(a,\cdot),\qquad
 Z_N(a,y)=c(X)^T f(y),\qquad n\in\mathbb Z.
 \tag{12}
\]
Here \([f_0]\) denotes the coefficient in this particular basis.
The exact source has incoming Laurent band \([-D,0]\), and
so does \(\mathcal A_{n,N}\).

Retain the original Newton vector \(v(w)\), coefficient
reversal \(J\), crossing multiplication \(M\), and
\(S=D_0M\), where
\[
       (D_0)_{ll}=\frac{\kappa^{-1}(-q)^{-l}}{P_l}.
 \tag{13}
\]
The whole terminal polynomial is
\(\mathcal V_{1,N}(w,X)=c(X)^T S v(w)\), as proved in
[the terminal-source identification](research_mixed_fourier_crossed_endpoint_terminal_source.md).
Let \(\mathsf T\) reverse the Newton coefficients and let
\(\mathsf R^k\) mean multiplication by the original signed
crossing power in the full quotient algebra.

**Theorem.** For every signed integer \(n\),
\[
 \boxed{\begin{split}
 \mathcal A_{n,N}(X)
     &=\kappa c(X)^T S M^{n-1}\mathbf e_0\\
     &=\kappa\bigl(\mathsf T\mathsf R^{\,n-1}\mathsf T\,
                         \mathcal V_{1,N}(\,\cdot\,,X)\bigr)(c_0)\\
     &=\kappa\phi_N\!\left(
                  R^{\,n-1}\mathsf T\mathcal V_{1,N}(\,\cdot\,,X)
                         \right),
       \qquad c_0=q+q^{-1}.
 \end{split}}
 \tag{14}
\]
In particular, only \(n=1\) here reduces immediately to the
unchanged terminal value \(\kappa\mathcal V_{1,N}(c_0,X)\).
The operations in the other lines must be retained.

*Proof.* The original Fourier dual gives
\[
 \mathcal M_n Z_N(a,y)
                =c(X)^T S M^n S^{-1}f(y).
 \tag{15}
\]
Since \(S^{-1}\mathbf e_0
=M^{-1}D_0^{-1}\mathbf e_0=\kappa M^{-1}\mathbf e_0\),
the first line of (14) follows.
Writing the Newton coefficient column of \(\mathcal V_1\)
as \(d(X)\), its transformed column is
\[
       J M^{n-1}J\,d(X)=(M^{n-1})^T d(X).
 \tag{16}
\]
This uses the original identity \(M^T=JMJ\), valid for
signed powers as well. As \(v(c_0)=\mathbf e_0\),
evaluation of (16) at \(c_0\) proves the second line.
Finally evaluation of a turned polynomial at \(c_0\)
selects its original last Newton coefficient, which is
\(\phi_N\) of the unturned polynomial.
Equivalently \(\phi_N(e_i e_j)=J_{ij}\) proves the last
line directly. These are identities in the full Hermite
algebra, not its reduction to distinct nodes. \(\square\)

The same dictionary has a useful physical-input form. At
\(X=r^b\), \(0\le b<N\), equation (2) of
[Gram transport](research_mixed_terminal_gram_shift.md) gives
\[
 \mathcal V_{1,N}(w,r^b)
       =\frac{(-q)^{-b}}{\kappa^2N}
                  (M^*M^3v(w))_b .
 \tag{17}
\]
Equality for every ordinary \(w\) identifies its full coefficient
row. Consequently (14) becomes
\[
 \boxed{\quad
 \mathcal A_{n,N}(r^b)
      =\frac{(-q)^{-b}}{\kappa N}
                    (M^*M^{n+2}\mathbf e_0)_b .
 \quad}
 \tag{18}
\]
All \(N\) physical values determine the unique Laurent
polynomial of band \([-D,0]\), so (18) is also a complete
dictionary for the entire incoming source, without a new
off-grid representative.

For comparison, the existing arbitrary terminal-power polynomial
\(\mathcal H_{p,N}=\mathsf T(R^p)\) has coefficient column
\(\mathbf h^{(p)}=JM^p\mathbf e_0\). Thus (18) equivalently is
\[
 \mathcal A_{n,N}(r^b)
      =\frac{(-q)^{-b}}{\kappa N}
                    (M^*J\,\mathbf h^{(n+2)})_b .
 \tag{19}
\]
The old \(q\)-binomial chain sums and conjugate negative-power
formulas compute \(\mathbf h^{(p)}\) exactly. They do not
remove the observation \(M^*J\) or identify (19) with the
bare value \(\mathcal H_{n+2,N}(c_0)\).
This is the same distinction already made for the ordinary
terminal source in Gram transport, Section 1.
The clock conjugations in
[quantum continuants](research_crossing_run_quantum_continuants.md)
likewise retain their original endpoint forcing; no norm
conclusion is imported from their sparse realization.

As an exact normalization check at a nontrivial signed shift,
\[
       \mathcal A_{-2,N}(X)
             =\frac{\kappa^{-2}}{N^2}
                          \sum_{j=0}^{D}X^{-j}.
 \tag{20}
\]
Indeed \(M^*\) is upper triangular and its first column is
\(\kappa^{-1}\mathbf e_0\). Equation (18) at \(n=-2\)
therefore has value \(\kappa^{-2}/N\) at \(b=0\) and zero
at all other physical incoming nodes. The geometric polynomial
in (20) has exactly those values and the correct Laurent band.
This check does not discard the ordinary normals of any
matrix used in deriving it.

## 4. The precise additional analytic observation

The last line of (14) is also an exact full Hermite contour.
Let \(\mathscr Q_N(z)=2T_N(z/2)+2\), with \(T_N\) the usual
Chebyshev polynomial, and let \(R_N^{[k]}(z)\) be the degree
less than \(N\) representative of \(R^k\) in the original
quotient, for every signed \(k\). Then
\[
 \mathcal A_{n,N}(X)
   =\frac{\kappa(-1)^D N^2}{2\pi i}
      \oint_{\mathcal C}
       \frac{R_N^{[n-1]}(z)
                 (\mathsf T\mathcal V_{1,N})(z,X)}
            {\mathscr Q_N(z)}\,dz ,
 \tag{21}
\]
where \(\mathcal C\) encloses all original quotient nodes.
This follows from
\(\phi_N(F)=(-1)^DN^2[z^D]\operatorname{rem}_{\mathscr Q_N}F\).
At double nodes, the contour retains the original first
normal. In particular a negative power in (21) is its
canonical polynomial representative, not an uncontrolled
rational continuation outside the quotient.

Thus a lower asymptotic for this specific observation requires
analysis of (21), or an equivalent complete source (11):
one must identify a nonzero leading observed coefficient and
bound all of its complementary currents against that same
action. A packet for \(\mathcal H_{n+2,N}\) at one ordinary
color alone does not bound \(M^*J\mathbf h^{(n+2)}\).
Conversely, if the aim is to discard the first coefficient
while propagating the crossed Fourier source, the needed
quantity is exactly
\[
             \Pi_0\mathcal M_nZ_N(a,y)
                       =\mathcal A_{n,N}(X)f_0(y).
 \tag{22}
\]
Its rate includes the \(f_0(y)\) contribution \(\pi\Im y\)
near the original Fourier output. The known \(n=0\) projection
gap and the \(n=1\) ordinary-terminal upper estimates do not
automatically iterate to (22) for other signed \(n\).
None of these exact identities asserts failure of a desired
gap, a new nonzero crossing packet, or arbitrary short-filling
stability.
