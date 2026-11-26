# A factorized contour for the same finite crossing block

Research deduction, 7 November 2026. The homogeneous remainder can
be changed by a multiple of its second period so that its contour
has a simpler pair of joining terms. The changed function has exactly
the same values at every pair of physical colors. It therefore
represents the same complete finite crossing matrix, including the
ordinary derivatives carried by its specified matrix adapters.

This statement concerns the complete finite matrix. The new function
is not the original finite Fourier polynomial away from its sampling
points. The reconstruction formula below recovers that polynomial
and all its derivatives. A separate estimate of the new contour and
its sampling corrections is still required; no new knot asymptotic
is inferred here.

## 1. The two factors of the exact period multiplier

Fix \(N\ge3\), put \(\delta=1/N\), \(r=e^{-2\pi i/N}\), and write
\[
 X=e^{-2\pi ia},\qquad W=e^{-2\pi iy},\qquad
 A=X^{-N},\quad B=W^N,\quad a_0=A-1,\quad b_0=B-1.
 \tag{1}
\]
The physical colors are \(a=b/N,\ y=c/N\), where
\(0\le b,c<N\). In particular \(A=B=1\) at every physical pair.
Use the original factorial \(\Pi_N\), its reciprocal \(E_N\), and
the exact row
\[
 T_N(s;a,y)=e^{2\pi iNas}
       \Pi_N(s+a)\Pi_N(s+y)E_N(a)E_N(y)E_N(s)^2.
 \tag{2}
\]
The [homogeneous-period theorem](research_mixed_three_fourier_conditional_homogeneous_period.md)
defines the complete homogeneous remainder \(H_N\) and the second
period
\[
 I_N(a,y)=\int_{\alpha_N-i\infty}^{\alpha_N+i\infty}
                    k_2(s)T_N(s;a,y)\,ds,\qquad
 \alpha_N=-\frac1{2N},\qquad
 k_2(s)=\frac{t}{(1-t)^2},\quad t=e^{-2\pi iNs}.
 \tag{3}
\]
Both functions extend to the product of strips
\[
 \mathcal S_N^2,\qquad \mathcal S_N=\{-1/(2N)<\Re z<1\}.
 \tag{4}
\]
Their defining tails converge locally uniformly there at fixed \(N\).
We make no uniform large-\(N\) assertion at the edges of (4).

The exact period relation factors as
\[
 T_N(s+1)=U_a(t)U_y(t)T_N(s),\qquad
 U_a(t)=\frac{A-t}{1-t},\qquad
 U_y(t)=\frac{1-Bt}{1-t}.
 \tag{5}
\]
Indeed \(\Pi_N(z+1)=(1-e^{-2\pi iNz})\Pi_N(z)\).
The chirp contributes \(A\), the two numerator factorials contribute
\((1-X^Nt)(1-W^Nt)\), and the denominator contributes
\((1-t)^{-2}\). This gives exactly (5).

Set
\[
 c_N(a,y)=a_0-b_0-\frac12a_0b_0,\qquad
 J_N(a,y)=H_N(a,y)-Nc_N(a,y)I_N(a,y).
 \tag{6}
\]
The coefficient \(c_N\) is \(\delta\)-periodic in both parameters.
Consequently \(J_N\) satisfies the same homogeneous difference and
mixed contiguity equations as \(H_N\), wherever those shifted
equations are defined. Its Casoratian with \(I_N\) is unchanged.

**Proposition 1.** For every finite real height \(h\), with
\(\beta_N=\alpha_N+1\), the new function has the exact contour
\[
 \begin{split}
 J_N={}&N\int_{\alpha_N+ih}^{\beta_N+ih}T_N(s)\,ds\\
 &+N\int_{\alpha_N+ih}^{\alpha_N+i\infty}
                         (U_a(t)-1)T_N(s)\,ds\\
 &+N\int_{\alpha_N-i\infty}^{\alpha_N+ih}
                         (1-U_y(t))U_a(t)T_N(s)\,ds .
 \end{split}
 \tag{7}
\]
Both vertical integrals are oriented upward.

*Proof.* The original contour for \(H_N\) has upper and lower
joining multipliers
\[
 K_+(t)=\frac{a_0-b_0t-a_0b_0t/2}{(1-t)^2},\qquad
 K_-(t)=\frac{t(a_0-b_0t+a_0b_0/2)}{(1-t)^2}.
 \tag{8}
\]
Direct subtraction gives
\[
 K_+-c_Nk_2=\frac{a_0}{1-t}=U_a-1,\qquad
 K_--c_Nk_2=\frac{b_0t(A-t)}{(1-t)^2}=(1-U_y)U_a.
 \tag{9}
\]
Subtracting the complete integral \(Nc_NI_N\) proves (7).
The new upper multiplier is \(O(t^{-1})\) as \(t\to\infty\);
the lower one is \(O(t)\) as \(t\to0\). Thus the same original
factorial bounds give convergent tails with rates
\(2\pi N(1-\Re y)\) and \(2\pi N(1-\Re a)\), respectively.
Their strict positivity on compact subsets of (4) justifies
the contour splitting. Alternatively, cut-independence follows
directly from
\[
 (U_a-1)-(1-U_y)U_a=U_aU_y-1
\]
and (5). \(\square\)

## 2. The complete finite matrix is unchanged

The particular term in
\[
 C_{0,N}(X,W)=H_N(a,y)+F_N^{\mathrm{part}}(a,y)
 \tag{10}
\]
has the factors \(a_0b_0\). The
[full-node theorem](research_mixed_three_homogeneous_period_full_node_composition.md)
therefore gives \(H_N(b/N,c/N)=C_{0,N}(r^b,r^c)\).
Since \(c_N=0\) at these same pairs, we have
\[
 \boxed{\quad
 J_N(b/N,c/N)=H_N(b/N,c/N)=C_{0,N}(r^b,r^c)
 \qquad(0\le b,c<N).
 \quad}
 \tag{11}
\]

This is the entire \(N\)-by-\(N\) matrix, not a subset of ordinary
colors or a quotient discarding normal directions. In the notation
of the full-node theorem, let \(\mathbf J\) denote this node matrix,
\(\mathsf P=\operatorname{diag}((r;r)_b)\),
\(\mathsf D=\operatorname{diag}((-q)^{-b})\), where
\(q=e^{\pi i/N}\). Keep its original change-of-basis matrix \(S\)
and original interface \(\mathsf B\). Then
\[
 A_2=S^{-1}\mathsf P^{-1}\mathbf J\mathsf D,\qquad
 A_2^2=S^{-1}\mathsf P^{-1}\mathbf J\mathsf B\mathbf J\mathsf D.
 \tag{12}
\]
All other crossing matrices and branching tensors stay in their
specified slots. Substitution of (11) in a finite matrix or tensor
contraction proves equality of the complete sources. Ordinary
boundary derivatives carried by the original columns and their
derivatives remain unchanged for the same reason.

Equality at only one physical parameter is weaker. For example,
when \(a=b/N\) but \(y\) is free, \(a_0=0\) and \(c_N=-b_0\), so
\[
 J_N(b/N,y)=C_{0,N}(r^b,W)+N(W^N-1)I_N(b/N,y).
 \tag{13}
\]
Thus the new contour cannot simply replace the original free-output
Fourier function.

There is a corrected representative that does retain a free output:
\[
 \begin{split}
 J_N^{\mathrm{in}}(a,y)
   &:=J_N(a,y)-Nb_0I_N(a,y)\\
   &=H_N(a,y)-Na_0(1-b_0/2)I_N(a,y).
 \end{split}
 \tag{13a}
\]
It satisfies the same homogeneous equations and obeys
\[
 \boxed{\quad
 J_N^{\mathrm{in}}(b/N,y)=C_{0,N}(r^b,W)
 \quad(0\le b<N,\ y\in\mathcal S_N).
 \quad}
 \tag{13b}
\]
The second equality in (13a) follows from
\(c_N+b_0=a_0(1-b_0/2)\). At a physical incoming color both
this factor and \(F_N^{\mathrm{part}}\) vanish. This proves
(13b) as a holomorphic identity in the entire free output
domain, and therefore also proves equality of all its output
derivatives. Thus \(J_N^{\mathrm{in}}\), with the same original
outside scalar, can replace the conditional function in a finite
incoming-node contraction with a free output.

This correction retains the complete period \(Nb_0I_N\), whose
coefficient can have exponential size. No estimate permits dropping
it here. Incoming derivatives must still be reconstructed from the
original finite basis: equality in (13b) is at incoming nodes.

## 3. Cardinal reconstruction retains the original derivatives

The literal finite source has the rectangular Laurent band
\[
 C_{0,N}(X,W)
   =\sum_{j=0}^{N-1}
       \frac{X^{-j}(rX;r)_j(rW;r)_j}{(r;r)_j^2}
 \ \in\
 \operatorname{span}\{X^{-k}W^\ell:0\le k,\ell<N\}.
 \tag{14}
\]
Define the two cardinal polynomials
\[
 L_b^-(X)=\frac1N\sum_{k=0}^{N-1}(r^b/X)^k,\qquad
 L_c^+(W)=\frac1N\sum_{\ell=0}^{N-1}(Wr^{-c})^\ell.
 \tag{15}
\]
Each is one at its designated node and zero at the other \(N-1\)
nodes. Consequently
\[
 \boxed{\quad
 C_{0,N}(X,W)=
       \sum_{b,c=0}^{N-1}
              L_b^-(X)L_c^+(W)J_N(b/N,c/N).
 \quad}
 \tag{16}
\]
To prove uniqueness, apply the one-variable root-of-unity Fourier
inversion in each coordinate to the band (14). Equation (11) then
proves (16). No off-grid equality of \(J_N\) and \(C_{0,N}\) is used.

All parameter derivatives of the original \(C_{0,N}\) follow by
differentiating the finite cardinal weights in (16). The specified
ordinary normal adapters may instead be applied directly to (12).
Both procedures retain the original finite state.

Direct differentiation of \(J_N\) would give a different answer.
At a physical pair,
\[
 \partial_a c_N=\partial_y c_N=2\pi iN,
 \qquad
 \partial_a(J_N-H_N)=\partial_y(J_N-H_N)
                              =-2\pi iN^2I_N(b/N,c/N).
 \tag{17}
\]
The [physical-moment theorem](research_mixed_three_second_period_physical_moments.md)
proves that the last period value is nonzero. The first derivatives
of \(F_N^{\mathrm{part}}\) vanish at a physical pair, so this also
exhibits the difference from the corresponding raw derivatives of
the original \(C_{0,N}\).

## 4. The sampling correction vanishes as a complete contour

There is a useful exact check on any subsequent contour argument.
Choose closed contours \(\mathcal C_a,\mathcal C_y\) inside (4)
enclosing all their respective physical nodes and no other zeros
of \(a_0,b_0\). Let \(f(a,y)\) be holomorphic on and inside their
product. The correction in (6) satisfies
\[
 \int_{\mathcal C_a}\int_{\mathcal C_y}
     \frac{f(a,y)(J_N-H_N)}{a_0b_0}\,dy\,da=0.
 \tag{18}
\]
Indeed
\[
 \frac{c_N}{a_0b_0}=\frac1{b_0}-\frac1{a_0}-\frac12.
 \tag{19}
\]
For the first term, integrate in \(a\): there is no pole.
For the second term, integrate in \(y\). The constant term is
holomorphic in both variables. Holomorphy of \(I_N\) on (4)
justifies each step. Equivalently, the double residues vanish
because the correction is zero at every physical pair.

The zero in (18) concerns the whole closed contour. If its pieces
are moved separately to critical contours, all connecting pieces
must still be retained. It does not say that each resulting
integral has small exponential rate. In Fourier language, the
same issue is cancellation among the additional sampling terms.
The new representative can therefore be used in the actual finite
source, but a proof based on its selected critical contour must
estimate the full sampling formula.

For the free-output representative (13a), the corresponding
one-variable check is simpler:
\[
 \frac{J_N^{\mathrm{in}}-H_N}{a_0}
                       =-N(1-b_0/2)I_N.
 \tag{20}
\]
The right-hand side is holomorphic in \(a\) on (4). Its integral
against any holomorphic test function around \(\mathcal C_a\)
therefore vanishes. This is the exact incoming sampling correction
for (13b). A subsequent deformation must again retain the entire
closed contour.

The next analytic question is whether (7), together with these
sampling corrections in the actual adjacent contraction, has a
nonzero contribution at the required geometric action. The
identities above remove the need to insist on one particular
off-grid representative; they do not answer that question.
