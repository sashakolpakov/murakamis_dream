# The actual source at the boundary of a crossing run

Research note, 3 November 2026.

The uniformly bounded endpoint response of a crossing run is not
its crossing state. The state is selected by a resonant boundary
condition. This note identifies that condition and derives a
fixed-channel transfer for every entry of every fixed signed
crossing power. It includes the original phases, the initial
source, all Newton colors, and the full boundary polynomial.

At the actual input color zero, its apparent poles cancel
algebraically. The resulting transfer matrices have coefficients
bounded independently of the quantum level. This removes a
singular-coordinate problem; it does not prove that the complete
coherent product has the geometric exponential rate.

## 1. The resonant pencil and its normalization

Use \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(\eta=(-1)^D\), and the original crossing \(M\), including
\(\kappa=q^{D^2/2}\). Let \(X\) be the Newton clock
\(X\mathbf e_j=Q^j\mathbf e_j\).
The [quantum continuants](research_crossing_run_quantum_continuants.md)
give, for positive \(p\),
\[
 Y_p=M^pX^{-1}M^{-p}=A_p B_p^{-1},
 \tag{1}
\]
where
\[
 (A_p,B_p)=
 \begin{cases}
 (P_m,P_{m-1}),&p=2m,\\
 (C_m,C_{m-1}),&p=2m+1 .
 \end{cases}
 \tag{2}
\]
The letter \(B_p\) in this note is the denominator in (1);
it is not the primitive upper bidiagonal cap coordinate.
Put \(s=\lfloor p/2\rfloor\). The exact diagonal formulas
in the continuant theorem imply
\[
 \boxed{\quad
    \det(A_p-\lambda B_p)=\eta^s(1-\lambda^N).
 \quad}
 \tag{3}
\]
Indeed each diagonal entry is its value at \(\lambda=0\)
times \(1-\lambda Q^j\), and the product of these factors
is \(1-\lambda^N\).

The clock eigenvalues \(\lambda_\ell=Q^{-\ell}\) are
distinct. Its transported projector is
\[
 \begin{split}
 \Pi_{p,\ell}
   &=-\mathop{\rm Res}_{\lambda=\lambda_\ell}
                      (Y_p-\lambda I)^{-1}\\
   &=\frac{B_p\,\operatorname{adj}(A_p-\lambda_\ell B_p)}
                 {N\eta^s\lambda_\ell^{N-1}}
     =M^p\mathbf e_\ell\mathbf e_\ell^TM^{-p}.
 \end{split}
 \tag{4}
\]
In particular, if
\[
           \mu_\ell=M_{\ell\ell}
                =\kappa(-1)^\ell q^{\ell(\ell+1)},
 \tag{5}
\]
the original full column is
\[
                 M^p\mathbf e_\ell
                         =\mu_\ell^p\Pi_{p,\ell}\mathbf e_\ell.
 \tag{6}
\]
The triangular inverse has diagonal \(\mu_\ell^{-p}\),
which proves (6). At \(\ell=0\), the actual source is
therefore
\[
 \boxed{\quad
 M^p\mathbf e_0=
     \frac{\kappa^p}{N\eta^s}
          B_p\,\operatorname{adj}(A_p-B_p)\mathbf e_0 .
 \quad}
 \tag{7}
\]
All signs and factors in (7) come from the literal source.

The simple clock spectrum in (4) is an auxiliary coordinate
calculation. It is not a projection to the distinct roots
of \(2T_N(z/2)+2\). The matrices \(M,Z\) still act on that
complete repeated-root algebra; their first normals are
retained throughout.

## 2. Every original matrix entry from a fixed-channel transfer

Let \(k=\lceil p/2\rceil\), and let \(T_k\) denote the
adjacency matrix of the path on \(k\) vertices. For
\(r\ne0\), define
\[
 \mathcal C_k(r)=(r+r^{-1})I_k-T_k-rE_{11},\qquad
 \mathcal H_k(r,\lambda)
                =\mathcal C_k(r)-q^{-1}\lambda E_{kk}.
 \tag{8}
\]
For \(k=1\), the two boundary modifications occur on the
same diagonal entry. Its determinant, at every \(k\), is
\[
       \det\mathcal H_k(r,\lambda)
                          =r^{-k}(1-q^{-1}\lambda r).
 \tag{9}
\]
To see this, the determinant before the last rank-one
change is \(r^{-k}\), and the last principal cofactor is
\(r^{-(k-1)}\).

At color \(j\), put
\[
 r_j=qQ^j,\qquad
 w_j=4\sin^2(j\pi/N)=(1-Q^j)(1-Q^{-j}),\quad 1\le j<N,
 \tag{10}
\]
and set
\[
 \mathcal D_j^{(p)}=
 \begin{cases}
 w_jI_k,&p\text{ even},\\
 \operatorname{diag}(1-Q^{-j},w_j,\ldots,w_j),
                                      &p\text{ odd}.
 \end{cases}
 \tag{11}
\]
Fix an input color \(\ell\), and define
\[
 v_{\ell,a}=r_\ell^{k-a},\quad 1\le a\le k,\qquad
 \mathcal G_j^{(\ell)}
          =\mathcal H_k(r_j,Q^{-\ell})^{-1}\quad(j>\ell).
 \tag{12}
\]
All inverses in (12) exist, since (9) vanishes exactly
when \(j=\ell\) in the finite color interval.

**Theorem 1.** Start \(u_\ell=v_\ell\) and propagate only
through the original remaining colors:
\[
          u_j=\mathcal G_j^{(\ell)}\mathcal D_j^{(p)}u_{j-1},
                    \qquad \ell<j<N.
 \tag{13}
\]
Then
\[
 \boxed{\quad
       (M^p)_{j\ell}=\mu_\ell^p\,\mathbf e_k^Tu_j
                       \quad(j\ge\ell),\qquad
       (M^p)_{j\ell}=0\quad(j<\ell).
 \quad}
 \tag{14}
\]
Here \(\mathbf e_k\) is the last coordinate of the
\(k\)-channel space, numbered from \(1\) to \(k\).
Negative powers are obtained by complex conjugating
every coefficient and initial datum in (13)--(14).

*Proof.* Take the even or odd block system from the
continuant theorem and subtract \(\lambda I_N\) from
its last stage diagonal. Its final Schur complement is
\(Y_p-\lambda I_N\). Divide the full block system by
\(q\), then order by color first and stage second.
Its diagonal color blocks are exactly (8). Its
subdiagonal blocks are minus (11). For an odd run the
first stage comes from \(-K\), whose subdiagonal is
\(-(1-Q^{-j})\); all later stages come from \(Z\), with
subdiagonal \(-w_j\). This proves the odd entry of (11)
as well as the even one.

The color \((i,\ell)\) block of the inverse, for
\(i\ge\ell\), is
\[
 q^{-1}\mathcal G_i(\lambda)\mathcal D_i^{(p)}
      \cdots\mathcal G_{\ell+1}(\lambda)
                   \mathcal D_{\ell+1}^{(p)}\mathcal G_\ell(\lambda),
 \tag{15}
\]
where \(\mathcal G_j(\lambda)=\mathcal H_k(r_j,\lambda)^{-1}\).
At \(\lambda=Q^{-\ell}\), only the last factor has a pole.
Its right and left nullvectors are both \(v_\ell\):
the first row uses \(r_\ell^{-1}v_{\ell,1}=v_{\ell,2}\),
the interior rows use the geometric progression, and the
last row uses \(v_{\ell,k-1}=r_\ell v_{\ell,k}\).
Since \(v_{\ell,k}=1\),
\[
 \mathop{\rm Res}_{\lambda=Q^{-\ell}}\mathcal G_\ell(\lambda)
                          =-q\,v_\ell v_\ell^T.
 \tag{16}
\]
This also follows from (9); the derivative in the
kernel directions is
\(v_\ell^T(-q^{-1}E_{kk})v_\ell=-q^{-1}\).
Thus the explicit \(q^{-1}\) in (15) cancels exactly.

Select the last stage in both color blocks of (15),
take minus its residue, and use (4)--(6). The result
is (13)--(14). The row \(j=\ell\) gives
\(\mu_\ell^p\) because the last entry of \(v_\ell\)
is one. The original identity \(\overline M=M^{-1}\)
proves the negative-power statement. \(\square\)

For an even run, one may pull all \(w_j\) outside the
product in (13); their product is \((S_i/S_\ell)^2\),
where \(S_i=\prod_{a=1}^i2\sin(a\pi/N)\).
Keeping (11) inside the transfer is more useful for
the odd case and for removing the apparent pole below.

Because Theorem 1 is an identity of the full original
matrices, it remains valid before attaching any
polynomial free-boundary evaluations. In particular
\(v_N(z)^TM^pv_N(w)\), with the original Newton
evaluation vector \(v_N\), is an ordinary polynomial
identity in both variables. All their mixed normal
derivatives are retained. The original compiler's
required \(J\) pairings can be applied to the same
matrix identity.

## 3. A transfer with no color poles at the actual input

At input \(\ell=0\), put
\[
 \mathcal B_k(r)
       =(1-r/q)\mathcal H_k(r,1)^{-1}
       =r^k\operatorname{adj}\mathcal H_k(r,1).
 \tag{17}
\]
The expression on the right is polynomial in \(r\) and
\(q^{-1}\): every cofactor has pole order at most
\(k-1\) at \(r=0\). In particular (17) remains defined
at \(r=q\); no singular inverse is used there.

With the prescribed initial vector
\[
                  u_0=(q^{k-1},q^{k-2},\ldots,1)^T,
 \tag{18}
\]
the actual source \((M^p)_{j0}=\kappa^p\mathbf e_k^Tu_j\)
has the exact recurrence
\[
 \boxed{\quad
 u_j=\mathcal T_j^{(p)}u_{j-1},\qquad
 \mathcal T_j^{(p)}=
 \begin{cases}
 (1-Q^{-j})\mathcal B_k(qQ^j),&p\text{ even},\\
 \mathcal B_k(qQ^j)
   \operatorname{diag}(-Q^{-j},1-Q^{-j},\ldots,1-Q^{-j}),
                                      &p\text{ odd}.
 \end{cases}
 \quad}
 \tag{19}
\]
The steps run from \(j=1\) through \(D\), exactly once.
To prove (19), divide (11) by \(1-Q^j\), using
\[
 \frac{w_j}{1-Q^j}=1-Q^{-j},\qquad
 \frac{1-Q^{-j}}{1-Q^j}=-Q^{-j}.
 \tag{20}
\]
These are exact identities before taking the endpoint
limit.

All step matrices in (19) are bounded uniformly in
\(N,j\) for the fixed power \(p\). One explicit bound is
\[
               \|\mathcal T_j^{(p)}\|
                          \le2k\,11^{(k-1)/2}.
 \tag{21}
\]
Indeed on \(|r|=|q|=1\), each row of (8) at
\(\lambda=1\) has Euclidean norm at most \(\sqrt{11}\).
Hadamard's inequality bounds each cofactor by
\(11^{(k-1)/2}\); the norm of the adjugate is at most
\(k\) times its largest entry, and the extra diagonal
factor in (19) has norm at most two.

The explicit polynomial entries in
[the two-run source transfer](research_two_run_source_transfer.md),
equations (4) and (7), sharpen this to
\(\|\mathcal T_j^{(p)}\|\le2k(2k-1)\).
They also give a bounded-coefficient recurrence for the literal
two-run scalar (22), retaining its color-zero source.

The initial vector in (18) must not be replaced by a
periodic continuation of the recurrence. For an even
run, its formally extended step at \(j=0\) is zero,
whereas the actual initial vector is nonzero.
The original finite source therefore remains an
inhomogeneous boundary condition, even though the
coefficient formula is periodic in the clock.

## 4. What an original turn joins

Let \(\alpha_a=M^a\mathbf e_0\) and
\(\alpha_b=M^b\mathbf e_0\), for any fixed signed
powers. The original bilinear Frobenius form has
matrix \(J\), so \((M^b)^TJ=JM^b\). Therefore the
literal two-run closing scalar is
\[
 \boxed{\quad
 \phi_N\!\left(R^bT(R^a)\right)
     =\mathbf e_D^TM^bJM^a\mathbf e_0
     =\alpha_b^T\alpha_a.
 \quad}
 \tag{22}
\]
Equations (18)--(19) retain every term of this pairing.
They give finite-channel input for its coherent
analysis, with dimensions depending on \(|a|,|b|\)
but not on \(N\). No conjugation may be inserted in
(22) for two same-sign runs.

When \(b=-a\), (22) becomes the known positive norm
\(\|\alpha_a\|^2\), because
\(\alpha_{-a}=\overline{\alpha_a}\). This reflection
class was already proved in
[the original positive Newton metric](actual_newton_turn_positive_gram.md);
it is not a new consequence or a new claimed class
of volume-conjecture results.

The complete endpoint theorem concerns the unmodified
matrix \(\mathcal C_k(r_j)\). The actual source in
(8) has the additional boundary term
\(-q^{-1}E_{kk}\). At the original colors,
\[
 \mathcal H_k(r_{D-j},1)
                  \ne\mathcal H_k(r_j,1)^\dagger
 \tag{23}
\]
in general: their last boundary coefficients are
\(-q^{-1}\) and \(-q\), respectively. Thus the
reflection used for the unmodified endpoint product
does not identify the source product (19) with a
positive diagonal response. The small size of this
boundary difference as \(N\to\infty\) does not justify
discarding it at the resonant source.

## 5. Scope and reproduction

This note supplies the full original run operator,
its source normalization, and the actual \(J\) pairing
in a form with no omitted colors or first normals.
The apparent color poles of the source transfer are
removed exactly. A geometric saddle or a lower bound
for the coherent sum (22) remains an additional
analytic theorem.

The [full-period source-jet identity](research_two_run_monodromy_source_jets.md)
identifies that retained reset with a marked zeroth, first, or second
monodromy derivative, including opposite signs. It does not replace
the reset by periodic homogeneous initial data.

The [original-matrix diagnostic](../experiments/check_resonant_crossing_run_source.py)
checks all entries at both parities, positive and
negative powers, the normalized source projector,
and free-boundary values and mixed derivatives.
Its [saved result](../repro/results/research-resonant-crossing-run-source.json)
is a normalization check, not an asymptotic proof.
