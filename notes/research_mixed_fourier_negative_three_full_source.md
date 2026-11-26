# Three negative crossings reduce the complete cap to the adjoint interface

Research deduction, 7 November 2026. This is an identity for the whole
original Fourier source. After three negative crossings the remaining
finite operator word is \(M^*\), between the original cardinal vectors.
It admits one explicit Newton/Cauchy sum and, at every physical incoming
node, a single finite product. No projection or channel is discarded.

The regular index phase of that sum has no interior critical point
when \(X\ne1\). This does not eliminate endpoint or pole contributions,
or prove an asymptotic for the complete source. Both level parities and
all finite scalars are retained. No numerical evaluation is used.

## 1. The complete operator word

Use the conventions of
[the complete negative-crossing sources](research_mixed_fourier_negative_crossing_full_sources.md):
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad r=Q^{-1},
 \quad \kappa=q^{D^2/2},\qquad N\ge2,
\]
\[
 P_j=(r;r)_j,\quad F_j=(Q;Q)_j,\quad
 \nu_j=(-1)^jq^{j(j+1)},\quad F_j=\nu_jP_j,
\]
\[
 X=e^{-2\pi ia},\quad Y=e^{2\pi iy},\quad
 p_j(X)=(rX;r)_j,\quad \rho_j(X)=X^{-j}p_j(X).
\tag{1}
\]
Let \(Z_N(a,y)=\sum_l C_{1,N}(X,r^l)f_l(y)\) be the original
complete cap, including the cardinal \(1/N\), and put
\(G_n=\mathcal M_nZ_N\). The crossing action is
\(c^TSM^nS^{-1}f\), with the original \(S=D_0M\).

The exact physical-input dictionary in
[the signed coefficient calculation](research_mixed_fourier_signed_crossing_coefficients.md),
and the full-row derivation in the negative-crossing note, give
\[
 G_n(b/N,y)=\frac{(-q)^{-b}}{\kappa^2N}
             \mathbf e_b^TM^*M^{n+3}h(y),\qquad 0\le b<N .
\tag{2}
\]
For every fixed \(y\), the complete source has incoming Laurent band
\([-D,0]\). Introduce its unique cardinal interpolants
\[
 L_b(X)=\frac1N\sum_{k=0}^D(r^b/X)^k .
\]
The original half-band cardinals satisfy exactly
\[
 h_b(a)=\frac1N\sum_{k=0}^D
          e^{2\pi i(k-D/2)(a-b/N)}
       =e^{-\pi iDa}(-q)^{-b}L_b(X).
\tag{3}
\]
Interpolating (2) therefore proves, for every integer \(n\),
\[
 \boxed{\quad
 G_n(a,y)=\frac{e^{\pi iDa}}{\kappa^2N}
                h(a)^TM^*M^{n+3}h(y).
 \quad}
\tag{4}
\]
In particular
\[
 \boxed{\quad
 G_{-3}(a,y)=\frac{e^{\pi iDa}}{\kappa^2N}h(a)^TM^*h(y)
     =\frac{e^{\pi iDa}}{\kappa^2N}
          \overline{C_N(\bar y,\bar a)} .
 \quad}
\tag{5}
\]
Here \(C_N(x,y)=h(x)^TMh(y)\) is precisely
[the original one-crossing interface](research_three_four_source_interface.md),
equation (2). The last expression is a holomorphic function of \(a,y\);
the conjugates are paired as displayed. The fixed matrix \(M^*\) is
the original conjugate transpose, not conjugation of a free parameter.
Equation (5) identifies a finite short-word reduction. It does not
assert preservation of the old cap's Gaussian state.

## 2. A single Newton/Cauchy sum

**Theorem 1.** At every \(N\ge2\), for all complex \(a,y\),
\[
 \boxed{\quad
 G_{-3}(a,y)=
 \frac{\kappa^{-3}e^{\pi iDy}}{N^2}(1-Y^{-N})
 \sum_{k=0}^D
       \frac{\rho_k(X)}{P_k(1-Y^{-1}r^{k+1})}.
 \quad}
\tag{6}
\]
All apparent output singularities are removable. The everywhere
finite form of the same identity is
\[
 \boxed{\quad
 G_{-3}(a,y)=
 \frac{\kappa^{-3}e^{\pi iDy}}{N^2}
 \sum_{k=0}^D\frac{\rho_k(X)}{P_k}
          \mathcal D_N(Y^{-1}r^{k+1}),\qquad
 \mathcal D_N(z)=\sum_{\ell=0}^Dz^\ell .
 \quad}
\tag{7}
\]
These are complete sums, not formulas for a single observed
coefficient. The incoming band is \([-D,0]\); the output has the
original half-band \([-D/2,D/2]\).

*Proof.* Conjugate the original interface formula at
\((\bar y,\bar a)\). Its scalar factors become
\[
 \widetilde c_a=N^{-1}e^{\pi iDa}(1-X^N),\qquad
 \widetilde c_y=N^{-1}e^{\pi iDy}(1-Y^{-N}),
\]
and the remaining sum is
\[
 \kappa^{-1}\widetilde c_a\widetilde c_y
 \sum_{i=0}^D
   \frac{X^iF_i}{(1-Y^{-1}Q^i)(X;Q)_{i+1}}.
\]
After multiplication by the scalar in (5), this is
\[
 \frac{\kappa^{-3}e^{\pi iDy}}{N^3}
 X^{-D}(1-X^N)(1-Y^{-N})
 \sum_{i=0}^D
   \frac{X^iF_i}{(1-Y^{-1}Q^i)(X;Q)_{i+1}}.
\tag{8}
\]
Use the exact polynomial cancellation and factorial complement
\[
 \frac{1-X^N}{(X;Q)_{i+1}}
       =\prod_{j=i+1}^D(1-XQ^j)=p_{D-i}(X),
 \qquad F_{D-k}=\frac{N}{P_k}.
\tag{9}
\]
The cancellation is a polynomial identity, including at its zeros.
The second equality follows from \(F_D=N\), by reversing its last
\(k\) factors. Setting \(k=D-i\), so \(Q^{D-k}=r^{k+1}\),
proves (6).

For each physical index \(k\), the \(N\)th power of
\(Y^{-1}r^{k+1}\) is \(Y^{-N}\). Hence the quotient in (6) is
exactly \(\mathcal D_N(Y^{-1}r^{k+1})\); this proves (7), including
every output root of unity. No division by a possibly zero weight
or finite numerator is used. \(\square\)

## 3. Closed products on all physical incoming nodes

**Proposition 2.** For every \(0\le b<N\),
\[
 \boxed{\quad
 G_{-3}(b/N,y)=
    \frac{\kappa^{-3}e^{\pi iDy}}{N}
       \frac{(r/Y)^b(Y;r)_b}{P_b}.
 \quad}
\tag{10}
\]
This includes \(b=0,D\) and both parities.

*Proof.* The original matrix entries and cardinal expansion are
\[
 M_{jb}=\kappa(-1)^jq^{j+b^2}{j\brack b}_Q,\quad j\ge b,
 \qquad
 h_j(y)=\frac{e^{-\pi iDy}}N(-q^{-1})^j
                     \sum_{k=0}^DY^kr^{jk}.
\]
Substituting them into (2) at \(n=-3\) gives
\[
 G_{-3}(b/N,y)=
 \frac{\kappa^{-3}e^{-\pi iDy}}{N^2}\nu_b^{-1}
 \sum_{k=0}^DY^k\sum_{j=b}^D
                 r^{j(k+1)}{j\brack b}_r .
\tag{11}
\]
The polynomial
\[
 {j\brack b}_r=\frac{(r^{j-b+1};r)_b}{P_b}
\]
vanishes at all \(j<b\), so the inner sum may be extended to
all \(N\) roots. Expand its numerator by the finite binomial theorem:
\[
 (r^{j-b+1};r)_b
  =\sum_{t=0}^b(-1)^t
       r^{t(t-1)/2+(1-b)t}{b\brack t}_r r^{jt}.
\]
Root orthogonality leaves exactly \(k+1+t=N\). Indeed
\(1\le k+1+t\le2N-1\), so there is no second multiple of \(N\).
Thus (11) becomes
\[
 \frac{\kappa^{-3}e^{-\pi iDy}}N
        \frac{\nu_b^{-1}Y^D}{P_b}
                  (r^{1-b}Y^{-1};r)_b .
\]
Reversing this last product gives
\[
 (r^{1-b}Y^{-1};r)_b
   =(-Y^{-1})^br^{-b(b-1)/2}(Y;r)_b,\qquad
 \nu_b^{-1}(-Y^{-1})^br^{-b(b-1)/2}=(r/Y)^b.
\]
Since \(e^{-\pi iDy}Y^D=e^{\pi iDy}\), (10) follows.
All factorial denominators have index below \(N\). \(\square\)

One exact consequence records the finite endpoint forcing.
Normalize
\[
 H_N(X;Y)=\kappa^3N e^{-\pi iDy}G_{-3}(a,y).
\]
As a Laurent polynomial in \(X\), it satisfies
\[
 \boxed{\quad
 (1-rX)H_N(rX;Y)-(r/Y-rX)H_N(X;Y)
   =\frac{1-Y^{-N}}{N^2}
           \sum_{k=0}^D(r^{-1}/X)^k .
 \quad}
\tag{12}
\]
To prove this, (10) gives zero on the left at \(X=r^b\) for
\(b<D\). At \(b=D\) it gives \((1-Y^{-N})/N\).
The operator on the left preserves band \([-D,0]\): its potential
\(X^1\) terms cancel. Cardinal interpolation proves (12).
In particular the endpoint forcing cannot be omitted when using the
product recurrence away from the physical grid.

## 4. The regular phase and its limitation

Let \(s=k/N\). Consider a compact index chart on which the original
factorial packets for \(P_k\) and \(p_k(X)\) are regular, with their
original lifts, and with
\[
 1-e^{-2\pi is}\ne0,\qquad
 1-Xe^{-2\pi is}\ne0,\qquad
 1-Y^{-1}e^{-2\pi i(s+1/N)}\ne0 .
\tag{13}
\]
For example one can use a compact subset of the original factorial
strips for \(s,a,s+a\), separated from their endpoint and cut
divisors, and keep a fixed distance from the last divisor in (13).
Only on such a separated chart is the Cauchy factor in (6) a
uniformly bounded analytic amplitude. The index-dependent
exponential phase there is
\[
 \mathscr S(s;a)=g(s+a)-g(a)-g(s)+2\pi ias,
 \qquad g'(z)=\log(1-e^{-2\pi iz}),
\tag{14}
\]
using the same original primitive as the negative-crossing source
note. The scalar depending on \(y,N\) in (6) is independent of \(s\).
Writing \(U=e^{-2\pi is}\), one obtains the branch-independent identity
\[
 \exp\mathscr S_s(s;a)=\frac{1-XU}{X(1-U)}.
\tag{15}
\]
If \(X\ne1\), the right-hand side is never \(1\).
Consequently \(\mathscr S_s\) cannot vanish on any regular
logarithmic lift. In particular this applies to the actual incoming
typed domains, which exclude \(X=1\).

This is not an absence theorem for geometric contributions.
The rational interpolation of (6) has moving poles
\[
             s=\ell-y-\frac1N,\qquad \ell\in\mathbb Z .
\tag{16}
\]
Their \(1/N\) displacement, and the possibly large Cauchy factor on
shrinking neighborhoods, must be retained in any contour argument.
The entire geometric form (7) agrees at physical indices, but its
off-grid numerator is
\[
       1-Y^{-N}e^{-2\pi iNs},
\]
whereas (6) has the fixed numerator \(1-Y^{-N}\). It is therefore
a different off-grid continuation; switching between them inside a
contour identity requires the exact correction. In particular the
physical cancellation of an apparent output singularity does not
remove the poles (16) from the rational index chart.

Thus (5)--(10) simplify the complete finite source, while (15)
specifies why an old interior Gaussian packet cannot simply be
reused for this representation. Endpoint terms, pole residues and
their cancellations remain possible. No asymptotic, global
nonvanishing, topology identification or attachment norm bound is
inferred here.
