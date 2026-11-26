# Necessary adjugate bounds and the first central spectral normal

This private continuation starts from `md-odd-cofactor-casimir-resolvent.md`. It gives exact necessary conditions for a constant Hermitian adjugate adapter and a concrete obstruction to replacing the first spectral derivative by a stable polynomial. It does not construct the adapter, bound its singular-value tail, or extend the one-cap theorem.

## 1. The source remains unchanged

Let \(N=2m+1\), \(\theta=\pi/N\),
\[
 s_j=2\sin(j\theta),\qquad a_j=4\cos^2((j+\tfrac12)\theta).
\]
The original row-replacement polynomials are
\[
 R_0=1,\qquad
 R_j=b^j\prod_{r<j}(a_r+u)+s_j^2(x+y)R_{j-1}
       +s_js_{j-1}(a_{j-1}+u)xyR_{j-2},
\]
with the final term omitted at \(j=1\). Set \(G_b(u)=R_m(b;u)\), \(D_b(u)=R_{m-1}(b;u)\). The actual central numerator is
\[
 P_C(u)=G_b(u)G_c(u)+u s_m^2xyD_b(u)D_c(u),\qquad \sigma=-2-u.
\]
In particular
\[
 P_C'(0)=G_b'(0)G_c(0)+G_b(0)G_c'(0)
             +s_m^2xyD_b(0)D_c(0).
\]
A prime here means differentiation in \(u\); the physical \(\sigma\)-derivative has the opposite sign. The last term is the central-skipping current and is retained.

The positive endpoint pencil is
\[
 M(b,x,y)=bI+\frac x2H_-+\frac y2H_+,
 \qquad G_b(0)=N\det M(b,x,y).
\]
The matrices and the scalar \(N\) are those of the original source determinant. No independent coefficient extraction has been introduced.

## 2. Exact constraints on any constant adapter

Suppose, only for this section, that a constant Hermitian matrix \(W\), independent of the face variables, satisfies
\[
 \frac{D_b(0)}N=\operatorname{Tr}(W\operatorname{adj}M(b,x,y)).
 \tag{1}
\]
The recurrence with \(y=0\) gives the exact necessary boundary identity
\[
 x\,\frac{D_b(0)}N
 =\frac{\det(bI+xH_-/2)-b^m}{s_m^2}.
 \tag{2}
\]
There is a corresponding identity with \(x=0\) and \(H_+\). These are polynomial equalities, including at zero face variables. They do not identify a common \(W\) from the two separate one-variable restrictions.

For \(N\ge5\), put \(J=(H_-+H_+)/2>0\). Reading the top two powers of \(b\) in the original forced Casimir equation gives
\[
 [b^{m-1}]\frac DN=\frac1{a_{m-1}},\qquad
 [b^{m-2}]\frac DN
   =\frac{s_{m-1}^2(x+y)}{a_{m-1}a_{m-2}}.
 \tag{3}
\]
For a fixed matrix \(K\),
\[
 \operatorname{adj}(bI+K)
 =b^{m-1}I+b^{m-2}(\operatorname{Tr}K\,I-K)+O(b^{m-3}).
\]
Consequently (1), specialized to \(x=y=1\), forces
\[
 \operatorname{Tr}W=\frac1{a_{m-1}},\qquad
 \operatorname{Tr}(WJ)
 =\frac{\operatorname{Tr}J}{a_{m-1}}
       -\frac{2s_{m-1}^2}{a_{m-1}a_{m-2}}.
 \tag{4}
\]
The diagonal of \(J\) is \(1/[\cos(j\theta)\cos((j+1)\theta)]\). Telescoping tangents therefore gives
\[
 \operatorname{Tr}J
 =\frac{\tan(m\theta)}{\sin\theta}
 =\frac1{2\sin^2(\theta/2)}.
\]
Also \(a_{m-1}=4\sin^2\theta\), \(a_{m-2}=4\sin^2(2\theta)\), and \(s_{m-1}=2\cos(3\theta/2)\). These identities reduce (4) to
\[
 \frac{\operatorname{Tr}(WJ)}{\operatorname{Tr}J}
 =\frac{4\cos\theta-1}{16\cos^2\theta\sin^2\theta}.
 \tag{5}
\]
For example the intermediate ratio subtracted from one is
\[
 \frac{2s_{m-1}^2}{a_{m-2}\operatorname{Tr}J}
   =\left(1-\frac1{2\cos\theta}\right)^2.
\]
Since \(J\) is positive definite and \(W\) is Hermitian,
\(|\operatorname{Tr}(WJ)|\le\|W\|\operatorname{Tr}J\). Thus every adapter (1) obeys the all-level necessary lower bound
\[
 \boxed{\quad
 \|W\|\ge
 \frac{4\cos\theta-1}{16\cos^2\theta\sin^2\theta}
 \sim\frac{3N^2}{16\pi^2}.
 \quad}
 \tag{6}
\]
A uniformly bounded adapter is impossible. This is compatible with the proposed singular-value bound \(s_k(W)=O(N^2/k^2)\); it does not prove that bound or disprove the existence of a controlled adapter. The trace condition alone would only give a lower bound of order \(N\) for the operator norm.

The top coefficient of the first visited-central normal is independently fixed:
\[
 [b^m]G_b'(0)
 =N\sum_{r=0}^{m-1}\frac1{a_r}
 =\frac{N(N^2-1)}{24}.
 \tag{7}
\]
Here \(a_r=s_{m-r}^2\), and the usual finite sine identity follows by logarithmically differentiating \(\sin Nz\) as a product of its translated sine factors. Thus an adapter for \(D\) alone would not settle the normal terms in the full numerator.

## 3. The first visited-central derivative need not be stable

This is a finite exact obstruction, not an asymptotic claim. At \(N=7\), set \(x=y=1\) and \(t=2\cos(\pi/7)\). The source recurrence gives
\[
 \begin{aligned}
 F(b):=G_b'(0)
 ={}&14b^3+(6t^2+10t+10)b^2\\
 &+(14t^2+7t-7)b+2t^2+8t-6.
 \end{aligned}
 \tag{8}
\]
The algebraic relation is \(t^3-t^2-2t+1=0\). It follows directly by factoring \(2\cos(7\theta)+2\) in \(t=2\cos\theta\). Reducing the cubic discriminant of (8) by this relation gives
\[
 \operatorname{disc}_b F
 =-196(1069t^2-2227t+685).
 \tag{9}
\]
The relevant root satisfies \(t>9/5\). Indeed \(t>\sqrt3\), the polynomial \(z^3-z^2-2z+1\) is strictly increasing there, and its value at \(9/5\) is \(-1/125\). The quadratic in parentheses is increasing for \(z\ge9/5\), and its value at \(9/5\) is \(3499/25\). Therefore
\[
 \operatorname{disc}_b F<-\frac{685804}{25}<0.
\]
The real cubic has a nonreal conjugate pair. Hence a statement that every first spectral derivative is a real stable face polynomial is false already at a finite odd level. This does not rule out a signed compression expansion, nor an assertion that ignores finitely many levels.

The portable script `md-odd-adjugate-first-normal-exact.py` executes the original recurrence in \(\mathbb Q[t]/(t^3-t^2-2t+1)\), independently computes the discriminant from the resulting coefficients, and verifies the exact rational sign bounds. Its result file records this finite scope.

## 4. What remains open

The earlier adjugate fits are not a proof of (1). One additional bounded diagnostic tried the square basis of real adjugate entries with \(i+j\ge m-1\). At \(N=13\) this basis has condition number about \(3.46\cdot10^9\); its resulting adapter has norm about \(5.14\cdot10^5\), while the earlier unrestricted fit had norm about \(5\). This is a failure of that chosen reconstruction to give useful control, not an impossibility theorem for other adapters. The script is retained separately.

The shifted factorization
\[
 a_j+u=4\cos((j+\tfrac12)\theta+\eta/2)
          \cos((j+\tfrac12)\theta-\eta/2),
 \qquad u=2\cos\eta-2,
\]
identifies the rows whose scalar diagonal changes sign. It does not transform the last-row replacement into a positive face pencil. At \(\eta=0\), all lower diagonals are positive while the proper lower cofactor already has the independently proved nonreal-root obstruction. Any stable-bulk method must therefore retain its boundary correction, not merely delete the sign-changing scalar rows.

The missing statement is an exact, face-independent adapter (1) with a controlled singular-value tail, or an equally controlled signed compression expansion of the original parameter-dependent source. A polynomial operator norm alone does not supply the vanishing normalized perturbation cost needed for a fixed spectral neighborhood. Neither the scalar Casimir denominators nor the eigenvalues of the positive endpoint matrices establish the required connection. All original shared targets, spectral normals, and the central-skipping term remain in the task.
