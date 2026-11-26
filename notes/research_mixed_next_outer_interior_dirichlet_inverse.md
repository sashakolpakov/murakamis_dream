# A bounded interior Dirichlet inverse for the actual outer adjoint

Private finite-source theorem, 8 November 2026. The actual weighted
seven-term adjoint is uniformly accretive after zero extension on
any fixed compact interior color interval. Its finite Dirichlet
inverse consequently has norm at most \(1/3\), for every nodal
right-hand side. This includes the literal high-degree insertion
in the original outer observation, without an analytic-degree
cost or an approximation residual.

The original finite summation-by-parts formula then retains the
parity forcing and the outgoing endpoint terms. Those terms are
not bounded below their original rate here. This is an interior
inverse, not a global inverse or a volume asymptotic. No numerical
evaluation is used.

## 1. Original source and the finite matrix

Retain the notation and full source of
[the exact seven-term theorem](research_mixed_next_physical_inner_seven_term_recurrence.md):
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad
 \kappa_N=q^{D^2/2},\quad
 m=\lfloor N/2\rfloor,\quad U=m-1,\quad M=\lceil N/2\rceil,\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 u_{j,N}=\pi-(2j+1)\pi/N,\qquad
 q_{j,N}=Q_N^{\rm full}(c_j),\\
 \mu_{j,N}=(-1)^U\kappa_N^3\omega_N(u_{j,N})
                                      q^{3j(j+1)},\\
 \omega_N(u)=
 \begin{cases}
 \sin u,&N\ \text{even},\\
 \sin u\sin(u/2)/\cos^2(\pi/(2N)),&N\ \text{odd}.
 \end{cases}
\end{gathered}                                                     \tag{1}
\]
These physical values also equal the full-first,
shortened-second inner values used in the original outer
contraction. The full-quotient equation retains the first normals
before restriction to its regular interior nodes.

The original equation and its weighted bilinear adjoint are
\[
\begin{split}
 (\mathbf D_{3,N}f)_j
       &=\sum_{r=-3}^{3}d_{j,r,N}f_{j+r},\\
 (\mathbf D_{3,N}q)_j&=\mathfrak f_N,\qquad
 \mathfrak f_N=
 \begin{cases}
 4\kappa_N^3/N^2,&N\ \text{even},\\
 0,&N\ \text{odd},
 \end{cases}\\
 (\mathbf D_{3,N}^{\dagger}h)_i
       &=\sum_{r=-3}^{3}
          \frac{\mu_{i-r,N}}{\mu_{i,N}}
                       d_{i-r,r,N}h_{i-r}.
\end{split}                                                       \tag{2}
\]
No conjugation is used in the last identity: it is the exact
adjoint for the original complex weights \(\mu_{j,N}\).

Fix a compact interval \(J\Subset(0,\pi)\). Let
\(I_N=[a,b]\cap\mathbb Z\) be any nonempty index interval with
\(u_{j,N}\in J\) for every \(j\in I_N\). All constants and
large-level thresholds below depend on \(J\), not on the
length or position of \(I_N\) within this condition. For
sufficiently large \(N\), the six-index neighborhood of \(I_N\)
lies in the regular ranges of the original recurrence and its
coefficients.

For \(f\in\mathbb C^{I_N}\), let \(\widetilde f\) be its zero
extension to the integers. Define the actual square matrix
\[
 (A_{I_N,N}f)_i
  =(\mathbf D_{3,N}^{\dagger}\widetilde f)_i
  =\sum_{r=-3}^{3}a_{i,r,N}\widetilde f_{i-r},
 \qquad
 a_{i,r,N}=
       \frac{\mu_{i-r,N}}{\mu_{i,N}}d_{i-r,r,N},
 \quad i\in I_N.
                                                                  \tag{3}
\]
This is a Dirichlet compression of the exact weighted adjoint.
It is not a new boundary condition on the original source \(q\).

Use the ordinary auxiliary Hilbert norm
\[
 \langle f,g\rangle=\sum_{i\in I_N}\overline{f_i}g_i,\qquad
 \|f\|_2^2=\langle f,f\rangle.
                                                                  \tag{4}
\]
The use of (4) to bound a finite matrix does not identify the
original bilinear trace with a positive inner product.

## 2. The actual slowly varying coefficients

The adopted
[all-character theorem](research_mixed_next_outer_all_character_symbol.md)
gives analytic coefficient functions \(b_{r,p}(u,\epsilon)\),
one formula for each parity, such that
\[
 a_{i,r,N}=b_{r,p}(u_{i,N},N^{-1}),\qquad
 b^0_r(u):=b_{r,p}(u,0).
                                                                  \tag{5}
\]
The leading coefficients \(b^0_r\) are common to both parities.
The exact ratio in (3) is retained in (5):
\[
 \frac{\mu_{i-r,N}}{\mu_{i,N}}
   =(-1)^r e^{3iru_{i,N}+3\pi i r^2/N}
       \frac{\omega_N(u_{i,N}+2\pi r/N)}
            {\omega_N(u_{i,N})}.
                                                                  \tag{6}
\]
In particular the rapidly varying crossing weight itself is
not replaced by its positive amplitude.

On a fixed slightly larger compact real interval
\(J'\Subset(0,\pi)\), containing \(J\) in its interior,
the analytic coefficient theorem supplies constants
\(C_0,C_1,C_2\), common to both parities and every
\(|r|\le3\), with
\[
\begin{gathered}
 |a_{i,r,N}|\le C_0,\qquad
 |a_{i,r,N}-b^0_r(u_{i,N})|\le C_1/N,\\
 \left|\frac{d}{du}b^0_r(u)\right|\le C_2
                      \qquad(u\in J').
\end{gathered}                                                     \tag{7}
\]
Only indices whose arguments lie in that fixed chart are used.
These bounds are a consequence of the actual analytic formulas,
including their finite shifts, not just a formal symbol expansion.

For completeness, put \(x=\cos u\) and
\(\alpha=\cot^2(u/2)\). The source theorem writes the original
leading polynomial as
\[
\begin{split}
 \ell(u,\zeta)&=2+2\alpha-\alpha(\zeta+\zeta^{-1}),\\
 m(u,\zeta)&=2+2\alpha
               -\alpha(e^{-iu}\zeta+e^{iu}\zeta^{-1}),\\
 d(u,\zeta)&=(\ell^2-1)m-(8+2x)\ell+10.
\end{split}                                                       \tag{8}
\]
It proves \(d(u,\zeta)\ge4\) for every real \(0<u<\pi\)
and every unit \(\zeta\), with the original ordered operator
and constants. Accordingly the frozen adjoint Fourier polynomial is
\[
 \sum_{r=-3}^{3}b^0_r(u)e^{-ir\vartheta}
       =d\bigl(u,-e^{i(3u-\vartheta)}\bigr)\ge4
           \qquad(\vartheta\in\mathbb R).
                                                                  \tag{9}
\]
The minus sign and \(3u\) in this formula are the exact physical
half-step and the original cubic crossing from (6). The sign of
\(\vartheta\) comes from the index shift \(f_{i-r}\) in (3).

## 3. A finite sliding-window proof of accretivity

**Theorem 1.** For all sufficiently large \(N\), for both
parities and every interval \(I_N\) specified above,
\[
 \boxed{\qquad
 \Re\langle f,A_{I_N,N}f\rangle\ge3\|f\|_2^2
            \qquad(f\in\mathbb C^{I_N}).
 \qquad}                                                        \tag{10}
\]

*Proof.* Work with the zero extension of \(f\). Put
\(L=\lfloor\sqrt N\rfloor\), and take \(N\) large enough that
\(L\ge4\). Define real windows
\[
 \chi_k(j)=L^{-1/2}\mathbf1_{\{k\le j<k+L\}},
 \qquad k\in\mathbb Z,\qquad f^{(k)}=\chi_k f .
                                                                  \tag{11}
\]
Only finitely many of these vectors are nonzero. Direct counting
gives the exact identities
\[
 \sum_k\chi_k(j)^2=1,\qquad
 \sum_k\chi_k(j)\chi_k(j-r)=1-\frac{|r|}{L}
                  \quad(|r|\le3).
                                                                  \tag{12}
\]
In particular \(\sum_k\|f^{(k)}\|_2^2=\|f\|_2^2\).

Write \(E_N(f)=\langle f,A_{I_N,N}f\rangle\).
Using zero extension, (12) gives
\[
 E_N(f)-\sum_k E_N(f^{(k)})
  =\sum_{i\in I_N}\sum_{r=-3}^{3}
       \frac{|r|}{L}\overline{f_i}a_{i,r,N}f_{i-r}.
                                                                  \tag{13}
\]
The estimate
\(\sum_i|f_i||f_{i-r}|\le\|f\|_2^2\) follows from
Cauchy--Schwarz on the zero-extended sequences. Since
\(\sum_{r=-3}^{3}|r|=12\), (7) therefore implies
\[
 \left|E_N(f)-\sum_k E_N(f^{(k)})\right|
                         \le\frac{12C_0}{L}\|f\|_2^2.
                                                                  \tag{14}
\]
No smooth partition or boundary approximation was used.

For each window meeting \(I_N\), choose a reference index
\(i_k\in I_N\cap[k,k+L-1]\), and put \(u_k=u_{i_k,N}\).
If \(f^{(k)}_i\ne0\), then
\[
 |u_{i,N}-u_k|\le2\pi L/N.
                                                                  \tag{15}
\]
Freeze the coefficients at \(u_k\) in the convolution operator
on finitely supported integer sequences:
\[
 (\mathcal A_k^0v)_i
          =\sum_{r=-3}^{3}b^0_r(u_k)v_{i-r}.
                                                                  \tag{16}
\]
For \(\widehat v(\vartheta)=\sum_jv_j e^{-ij\vartheta}\),
finite Fourier orthogonality and (9) give
\[
\begin{split}
 \langle v,\mathcal A_k^0v\rangle
 &=\frac1{2\pi}\int_{-\pi}^{\pi}
      d\bigl(u_k,-e^{i(3u_k-\vartheta)}\bigr)
                           |\widehat v(\vartheta)|^2\,d\vartheta\\
 &\ge4\|v\|_2^2.
\end{split}                                                       \tag{17}
\]
This quantity is real. There is no assumption that the
variable-coefficient finite matrix itself is self-adjoint.

Equations (7),(15) bound each difference between an actual
coefficient in a nonzero row of \(f^{(k)}\) and its frozen
coefficient by \(C_1/N+2\pi C_2L/N\). A second application
of Cauchy--Schwarz, summed over the seven shifts, gives
\[
 \Re E_N(f^{(k)})
 \ge\left(4-\frac{7C_1}{N}
                  -\frac{14\pi C_2L}{N}\right)\|f^{(k)}\|_2^2.
                                                                  \tag{18}
\]
Sum (18), then use (12),(14). The result is the explicit
finite estimate
\[
 \Re E_N(f)\ge
 \left(4-\frac{7C_1}{N}
          -\frac{14\pi C_2L}{N}
          -\frac{12C_0}{L}\right)\|f\|_2^2.
                                                                  \tag{19}
\]
With \(L=\lfloor\sqrt N\rfloor\), the three losses tend to zero.
The constants depend only on the fixed chart, so one sufficiently
large threshold makes their sum at most one, simultaneously for
all \(I_N\) and both parities. This proves (10). \(\square\)

## 4. Exact inverse for arbitrary nodal data

**Corollary 2.** The matrix \(A_{I_N,N}\) is invertible, and
\[
                   \|A_{I_N,N}^{-1}\|_{\ell^2\to\ell^2}
                                      \le\frac13.
                                                                  \tag{20}
\]
Indeed (10) and Cauchy--Schwarz imply
\(\|A_{I_N,N}f\|_2\ge3\|f\|_2\). This proves injectivity;
the matrix is square, so it proves invertibility and (20).

Thus for every \(g\in\mathbb C^{I_N}\), the exact solution
\[
                 h=A_{I_N,N}^{-1}g,\qquad
                 \|h\|_2\le\frac13\|g\|_2
                                                                  \tag{21}
\]
exists. No analyticity, polynomial degree, or frequency
restriction on \(g\) is needed.

For a true Fourier carrier \(g_i=e^{ibu_{i,N}}\), real \(b\),
the diagonal matrix with these entries is unitary. Its
conjugation of \(A_{I_N,N}\) has the same accretivity and
inverse bound. In particular every actual Chebyshev mode is
covered with its exact two characters:
\[
 T_b(c_i/2)=(-1)^b\cos(bu_{i,N})
       =\frac{(-1)^b}{2}
           \bigl(e^{ibu_{i,N}}+e^{-ibu_{i,N}}\bigr).
                                                                  \tag{22}
\]
The original sign or either Fourier character is not dropped.

More directly, take the literal nodal insertion
\[
                          g_i=H_N(c_i,Z_*).
                                                                  \tag{23}
\]
Here \(H_N\) is the unchanged polynomial of the
[outer Casimir observation, equation (5)](research_mixed_next_three_outer_casimir_observation.md);
its degree is less than \(N/3\). Formula (21) applies to all
its coefficients together. It does not replace \(H_N\) by a
partial packet or require a positive bound on its separate
Newton coefficients.

## 5. Original source reduction with outgoing endpoint terms

Extend the solution \(h\) of (21) by zero outside \(I_N\).
The original exact finite summation-by-parts identity then gives
\[
\boxed{\quad
 \sum_{i\in I_N}\mu_{i,N}g_iq_{i,N}
   =\mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j
                   -\mathcal B_{I_N}^{\rm out}(h,q),
 \quad}                                                          \tag{24}
\]
where
\[
 \mathcal B_{I_N}^{\rm out}(h,q)
  =\sum_{r=-3}^{3}
     \sum_{\substack{j\in I_N\\j+r\notin I_N}}
              \mu_{j,N}h_jd_{j,r,N}q_{j+r,N}.
                                                                  \tag{25}
\]
There is no approximation residual in (24).

To verify the boundary sign, the complete identity is
\[
 \sum_{j\in I_N}\mu_{j,N}h_j(\mathbf D_{3,N}q)_j
   =\sum_{i\in I_N}\mu_{i,N}
          (\mathbf D_{3,N}^{\dagger}h)_iq_{i,N}
                  +\mathcal B_{I_N}(h,q).
                                                                  \tag{26}
\]
The adjoint on \(I_N\) is exactly \(A_{I_N,N}h=g\).
The incoming part of \(\mathcal B_{I_N}\), whose coefficient
center \(j\) lies outside \(I_N\), vanishes because \(h_j=0\).
Its outgoing part is precisely (25), with the sign in (24).
The values \(q_{j+r,N}\) outside the chosen interval have not
been set to zero. They remain actual physical source values.

There are at most \(\sum_{r=-3}^{3}|r|=12\) pairs in (25).
They involve only the three inner and three outer indices
at each endpoint. All lie in the regular physical range for
large \(N\), by the fixed compact assumption on \(J\).

The even forcing has the explicit bound
\[
 \left|\mathfrak f_N\sum_{j\in I_N}\mu_{j,N}h_j\right|
  \le\frac{4}{3N^2}\|\mu\|_{2,I_N}\|g\|_2
  \le\frac{8}{3N}\|g\|_\infty.
                                                                  \tag{27}
\]
The first inequality uses (21), and the second uses
\(|\mu_{j,N}|=\omega_N(u_{j,N})\le2\) and
\(|I_N|\le N\). At odd levels the forcing is exactly zero.
For a single character or Chebyshev mode, \(\|g\|_\infty\le1\).

For the actual insertion (23), the adopted whole-real
polynomial bound is
\[
 \|g\|_\infty\le C_\tau N^{A_\tau}
                          e^{N(E_*+\tau)},\qquad
 E_*=\Lambda-\frac{2383}{1500}-\frac1{50}.
                                                                  \tag{28}
\]
Thus its even forcing has that same exponential ceiling and a
polynomial factor. The arbitrary-degree inverse itself adds
no exponential rate. The outgoing term (25) still requires
control with its original correlations.

For example, if \(D_J\) bounds the original \(d_{j,r,N}\)
on the relevant compact chart, Cauchy--Schwarz on the at most
twelve pairs gives a constant \(C_{\partial,J}\) with
\[
 |\mathcal B_{I_N}^{\rm out}(h,q)|
    \le C_{\partial,J}\|g\|_2
       \left(\sum_{i\in\{a-3,a-2,a-1,b+1,b+2,b+3\}}
                                    |q_{i,N}|^2\right)^{1/2}.
                                                                  \tag{29}
\]
This coarse bound is stated only to make the endpoint
dependence explicit; it need not meet the desired action budget.
The exact expression (25) retains more information.

## 6. Errors and the precise scope of the inverse

If \(p_j\) is a comparison sequence, put
\[
 e_j=q_{j,N}-p_j,\qquad
 \varepsilon_j=(\mathbf D_{3,N}p)_j-\mathfrak f_N.
                                                                  \tag{30}
\]
Using the same exact solved probe yields
\[
 \sum_{i\in I_N}\mu_{i,N}g_i e_i
   =-\sum_{j\in I_N}\mu_{j,N}h_j\varepsilon_j
                         -\mathcal B_{I_N}^{\rm out}(h,e).
                                                                  \tag{31}
\]
In particular the residual term is at most
\(\frac13\|g\|_2\|\mu\varepsilon\|_{2,I_N}\).
This is a finite correlated-error identity. A residual estimate
or endpoint error estimate for a proposed asymptotic packet is
not supplied by it.

All formulas keep the original outside factor
\((-q)^M/(\kappa_N^2N)\) when inserted into the transfer.
Both parity forcings, every source value in (25), and the
original full-Hermite normalization are unchanged.

Accretivity here concerns the actual weighted adjoint of the
seven-term constraint on a finite interior interval. It is not
a positive self-adjoint realization of the reduced crossing
operator, and does not turn the original observation into a
positive trace. The zero extension is imposed on the test
sequence only and creates exactly the retained terms (25).

The constants need not remain uniform as \(J\) approaches
zero or \(\pi\). The theorem does not impose or solve the
coalescing physical endpoint conditions of the full quotient,
give a global adjoint inverse, or bound the complete signed
outer observation at \(B_f\). It does remove the analytic
residual and degree cost from the fixed-interior adjoint
problem for the actual insertion.

### Source hashes

- Exact seven-term source and weighted summation by parts:
  49cd08c5759bd6669d3cbf1a7e661d60188639c9added0c973659c4723d0a21a.
- All-unit-character symbol and actual coefficient charts:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Exact outer insertion and scalar:
  cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab.
