# Exact single-factor projections and the limit of a separated spectral bound

The protected scalar has a positive non-diagonal moment form. The open spectral question is whether its dual norm stays polynomial on the whole real spectral interval. This note derives exact projections onto the already known single-factor orthogonal polynomials. It shows that bounding the two moment factors separately gives an exponentially large upper bound at a fixed interior spectrum. It does **not** show that the true, jointly defined spectral dual norm is large.

## 1. The original spectral vector and its moment form

Let
\[
 N\ge4,\quad d=N-1,\quad m=\lfloor N/2\rfloor,
 \quad M=m-1,\quad \theta=\pi/N,\quad q=e^{i\theta},\quad Q=q^2.
 \tag{1}
\]
Use the original protected coefficients
\[
 v_j(\sigma)=(-1)^j S_j^2\prod_{r=j+1}^d(\sigma-c_r),
 \quad c_r=2\cos((2r+1)\theta),
 \quad S_j=\prod_{r=1}^j2\sin(r\theta),
 \quad U_0=\csc^2(\theta/2).
 \tag{2}
\]
Set
\[
 b_j=\prod_{r=1}^j\frac{\sin(r\theta)}{\sin((r+1/2)\theta)},
 \qquad h_j=b_j^2,\qquad
 H_0=(b_{i+j})_{0\le i,j\le M},\qquad
 H=H_0\circ H_0.
 \tag{3}
\]
The circle denotes entrywise product. The positive beta-product construction in `research_flat_cap_positive_moment_form.md` proves that these are positive definite Gram matrices. The required largest degree is \(2M\le d\). No assumption of support in \([0,1]\) is used.

Write \(\ell(t^j)=b_j\) for the single-factor positive functional. Its orthogonal polynomials \(P_n\), normalized by \(P_n(0)=1\), and their norms were already derived in `md-cap-moment-cauchy-norm-obstruction.md`, §2. Explicitly,
\[
 P_n(t)=\sum_{j=0}^n
 \frac{(Q^{-n};Q)_j(qQ^n;Q)_j}{(Q;Q)_j^2}
                  q^{3j/2}t^j,
 \qquad
 \nu_n=\ell(P_n^2)
       =\frac{\sin(\theta/2)}{\sin((2n+1/2)\theta)}.
 \tag{4}
\]
Here \((a;Q)_j=\prod_{r=0}^{j-1}(1-aQ^r)\), and \(q^{1/2}=e^{i\theta/2}\) has its indicated lift. The coefficients in (4) are real: their successive ratio is
\[
 -\frac{\sin((n+j+1/2)\theta)\sin((n-j)\theta)}
        {\sin^2((j+1)\theta)}.
 \tag{5}
\]
For clarity, their orthogonality follows directly from the moment ratio. The operator
\[
 t^{-1}\bigl(\cos(2\theta t\partial_t)-1\bigr)
       -\cos\bigl(\theta(2t\partial_t+1/2)\bigr)
 \tag{6}
\]
is symmetric for \(\ell\). Its distinct diagonal eigenvalues on degrees \(0,\ldots,M\) are \(-\cos((2n+1/2)\theta)\). Comparing its coefficients gives (5); symmetry of multiplication by \(t\) then gives the telescoping norm (4). Thus the complex-looking notation in (4) does not import an orthogonality theorem for a complex measure.

The actual spectral vector and its squared dual norm are
\[
 g_j(\sigma)=\frac{(-1)^jv_j(\sigma)}{U_0},\qquad
 \kappa_N(\sigma)=g(\sigma)^T H^{-1}g(\sigma).
 \tag{7}
\]
For a real spectrum the vector is real. The desired bound on \(\kappa_N\) is not assumed below.

## 2. A factorization retaining the spectral phase

Take \(\sigma=2\cos\varphi\), \(0\le\varphi\le\pi\), and put \(a=\varphi/2\), \(w=e^{i\varphi}\). For \(\epsilon=\pm1\), define
\[
 \begin{aligned}
 C_\epsilon&=
       \frac{\sin(\theta/2)\cos(Na)}{\sin(\theta/2+\epsilon a)},\\
 F_j^\epsilon
   &=C_\epsilon e^{-i\epsilon ja}
       \prod_{r=1}^j
         \frac{\sin(r\theta)}{\sin((r+1/2)\theta+\epsilon a)}\\
   &=C_\epsilon q^{j/2}
             \frac{(Q;Q)_j}{(qQw^\epsilon;Q)_j}.
 \end{aligned}
 \tag{8}
\]
Initially these formulas are read away from their displayed zero denominators. Every apparent singularity is removable. Indeed the product identity
\[
 \prod_{r=0}^{N-1}\sin((r+1/2)\theta+\epsilon a)
                   =2^{1-N}\cos(Na)
 \tag{9}
\]
expresses (8) as a finite product of its unused factors. It is the same original unused-row cancellation as in (2), rather than a choice of a singular interpolation.

Using \(2\cos\varphi-2\cos((2r+1)\theta)
=4\sin((r+1/2)\theta+a)\sin((r+1/2)\theta-a)\), all phases in the product cancel and give
\[
                  g_j(2\cos\varphi)=F_j^+F_j^-.
 \tag{10}
\]
At \(\varphi=0\), both factors equal \(b_j\). At other real spectra each factor can be complex; it must not be replaced by its modulus before (10) is used.

## 3. Exact projections onto the known orthogonal basis

Define the two linear functionals \(L_\epsilon(t^j)=F_j^\epsilon\) on degrees at most \(M\). Then
\[
 \boxed{
 L_\epsilon(P_n)=
 C_\epsilon(qQ^n)^n
       \frac{(Q^{1-n}w^\epsilon;Q)_n}
            {(qQw^\epsilon;Q)_n}.}
 \tag{11}
\]
This is an exact terminating identity, including its continued values at all removable spectral singularities.

Here is a finite proof. Substitution of (8) into (4) cancels one factor \((Q;Q)_j\). The remaining sum is
\[
 \sum_{j=0}^n
   \frac{(Q^{-n};Q)_j(A;Q)_j}{(Q;Q)_j(C;Q)_j}Q^j
       =A^n\frac{(C/A;Q)_n}{(C;Q)_n},
 \quad A=qQ^n,quad C=qQw^\epsilon.
 \tag{12}
\]
To verify (12), multiply by \((C;Q)_n\). Both sides are monic polynomials of degree \(n\) in \(A\). At \(A=CQ^r\), \(0\le r<n\), the ratio \((A;Q)_j/(C;Q)_j=(CQ^j;Q)_r/(C;Q)_r\) is a polynomial of degree \(r\) in \(Q^j\). The finite binomial product
\[
 \sum_{j=0}^n\frac{(Q^{-n};Q)_j}{(Q;Q)_j}X^j
                    =(XQ^{-n};Q)_n .
 \tag{13}
\]
annihilates each of its terms after multiplication by \(Q^j\), since the relevant exponents are \(X=Q^{k+1}\) with \(0\le k<n\). These are precisely the \(n\) zeros of the right side of (12). Its leading coefficient is one after clearing the denominator, as is the \(j=n\) term on the left. This proves the identity by finite polynomial algebra. Formula (13) itself follows by multiplying its \(n\) linear factors, or by induction on \(n\).

Taking absolute values in (11) yields the explicit real product
\[
 |L_\epsilon(P_n)|=
 \sin(\theta/2)|\cos(Na)|
 \frac{\prod_{r=0}^{n-1}|\sin(\epsilon a-r\theta)|}
      {\prod_{r=0}^{n}|\sin(\epsilon a+(r+1/2)\theta)|}.
 \tag{14}
\]
Every original half shift is retained.

## 4. Why bounding the two factors independently loses exponentially

The squared dual norm of each factor on the single-factor Hilbert space is exactly
\[
 K_\epsilon=\sum_{n=0}^{M}\frac{|L_\epsilon(P_n)|^2}{\nu_n}.
 \tag{15}
\]
The tensor-product functional restricts, on the subspace spanned by \(t^ju^j\), to the spectral functional (10). Its Gram matrix there is \(H\). Hence it gives the valid upper bound
\[
                         \kappa_N(\sigma)\le K_+K_-.
 \tag{16}
\]
The upper bound (16), however, is exponentially large for a fixed interior spectrum. Take \(N\) divisible by eight, \(\sigma=0\), \(a=\pi/4\), and \(n=N/8\). Then \(|\cos(Na)|=1\). Formula (14) for the minus factor is
\[
 |L_-(P_n)|=
 \frac{\sin(\theta/2)}{\sin(a-(n+1/2)\theta)}
 \prod_{r=0}^{n-1}
       \frac{\sin(a+r\theta)}{\sin(a-(r+1/2)\theta)}.
 \tag{17}
\]
All displayed sine arguments lie in \((0,\pi/2)\). Every quotient is at least one. For \(r\ge\lceil n/2\rceil\), it is at least
\[
                  L=\frac{\sin(5\pi/16)}{\sin(3\pi/16)}>1.
 \tag{18}
\]
There are \(\lfloor n/2\rfloor\) such indices. Since \(\sin(\theta/2)\ge1/N\), and since the norms (4) satisfy \(0<\nu_n\le1\),
\[
 |L_-(P_n)|\ge N^{-1}L^{\lfloor N/16\rfloor},
 \qquad K_-\ge N^{-2}L^{2\lfloor N/16\rfloor}.
 \tag{19}
\]
The constant projection of the plus factor gives
\[
 K_+\ge |C_+|^2
    =\frac{\sin^2(\theta/2)}{\sin^2(a+\theta/2)}
    \ge N^{-2}.
 \tag{20}
\]
Consequently the separated upper bound itself obeys
\[
                     K_+K_-\ge N^{-4}L^{2\lfloor N/16\rfloor}.
 \tag{21}
\]
This is **not** a lower bound for \(\kappa_N\). The large tensor direction used in (19) need not lie in the diagonal subspace spanned by \(t^ju^j\). It proves precisely that separate single-factor dual bounds cannot give a polynomial estimate through (16). A successful estimate must retain the coupled restriction defining \(H\).

## 5. Scope and original-source dependence

All coefficients in (2), (7), and (10) are those of the original protected numerator. The other face targets remain in the spectator when this functional is applied. Neither the positive moment form nor the separated projection formula estimates the geometric rate of that spectator. The finite physical filling functional, with its node values and first normals, has not been replaced by a new invariant.

The source coefficient and exact sewn equation are in `md-protected-left-sharp-spectral-scalar.md`. The positive beta moment form is already public in `research_flat_cap_positive_moment_form.md`; the single-factor orthogonal polynomials and norms are already proved in `md-cap-moment-cauchy-norm-obstruction.md`. The finite Gram formulation in `md-protected-moment-gram.md` states the still open coupled spectral and spectator-energy estimates. The present addition is (11)–(21), not a new assertion of moment positivity, a spectral polynomial bound, or a volume theorem.
