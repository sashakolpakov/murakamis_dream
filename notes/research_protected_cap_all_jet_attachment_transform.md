# The exact all-jet cap adjoint on the entire attachment

Private written proof, 17 November 2026. The original signed crossing
at an adjacent protected corner can be eliminated with its protected
variables restored. Its replacement is a finite Jackson operator on
the entire neighboring attachment, followed by the exact phased merge.
The operator requires transverse attachment data; the fused value
alone does not determine it.

## 1. Original source and the finite target adjoint

Use the literal crossing polynomial of [J] and [C]. Set
\[
 N\ge3,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \sigma=\pm1,\quad \tau=q^{2\sigma},\quad
 a=-q^\sigma,\quad \lambda=\lambda_0^\sigma=q^{\sigma d^2/2}.
 \tag{1}
\]
The original square-root lift in \(\lambda\) is retained. In the
ordered quartet \(H_\sigma(X,Z,c,y)\), \(X\) is the protected outer
slot and \(Z\) the protected middle slot. The surviving ordinary
slots are \(c,y\). At the protected corner,
\[
 B(c,y)=H_\sigma(0,0,c,y)
       =\lambda\sum_{j=0}^d a^jc^{d-j}y^j.
 \tag{2}
\]
All these polynomials contain the actual root Hermite data.

Let \(F(X,Z,c,y;\mathbf z)\) be any polynomial attachment, with
arbitrary additional variables or coefficient parameters
\(\mathbf z\). The attachment may itself depend on \(X,Z\).
Every Jackson derivative below holds these external variables fixed.
Use \(D_{\tau,w}\) and \([k]_\tau!\) as in [J]. Only \(k<N\)
occurs, so their displayed factorial denominators are nonzero.

For \(I_d=[w^d]\), the exact adjoint is
\[
 I_d[(D_{\tau,w}f)g]
       =-\tau^{-1}I_d[fD_{\tau^{-1},w}g].
 \tag{3}
\]
Indeed a contributing pair of monomials has original degrees
\(r+s=d+1=N\), and
\([s]_{\tau^{-1}}=-\tau[r]_\tau\). This includes \(r=0,N\)
and \(s=0,N\): their zero factors are kept. Repeated application
gives the power \((-\tau^{-1})^k\); replacing \(\tau\) by its
inverse gives \((-\tau)^l\). There is no endpoint remainder or
change of the coefficient target.

## 2. Exact elimination with all protected jets

Define the finite operator on the attachment
\[
 \mathscr A_\sigma(X,Z)=
 \sum_{\substack{k,l\ge0\\k+l\le d}}
 \frac{(-\tau^{-1})^k(-\tau)^l X^kZ^l}
      {[k]_\tau![l]_{\tau^{-1}}!}
       D_{\tau^{-1},y}^{\,k}D_{\tau,c}^{\,l},
 \qquad
 (\mathscr M_a F)(t)=F(X,Z,at,t;\mathbf z).
 \tag{4}
\]
The order is essential: the derivatives act before
\(\mathscr M_a\). The exact original contraction is
\[
 \boxed{\quad
 [c^dy^d]\,H_\sigma(X,Z,c,y)F
      =\lambda[t^d]\,
          \mathscr M_a\bigl(\mathscr A_\sigma(X,Z)F\bigr).
 \quad} \tag{5}
\]
All coefficient operations in \(\mathbf z\) can be retained on both
sides. Thus (5) is an identity of full polynomial boundary sources,
not only a scalar evaluation or a truncated asymptotic expansion.

To prove it, the two commuting reconstructions of [J] give
\[
 H_\sigma(X,Z,c,y)
   =\sum_{k+l\le d}
       \frac{X^kZ^l}{[k]_\tau![l]_{\tau^{-1}}!}
       D_{\tau,y}^{\,k}D_{\tau^{-1},c}^{\,l}B(c,y).
 \tag{6}
\]
Move each derivative to the entire \(F\) by (3), in the same
variable and with target \(d\). Finally the exact cap identity
of [C] says
\[
 [c^dy^d]\,B(c,y)G(c,y)=\lambda[t^d]G(at,t)
 \tag{7}
\]
for every polynomial \(G\). This proves (5), including its scalar.
Terms with \(k+l>d\) vanish already in (6), since \(B\) has total
degree \(d\); none has been discarded from the original source.
No \(q\)-derivative or continuation away from the specified root is
used.

The ordinary product rule in the protected variables remains
necessary. Write \(F_0,F_X,F_Z,F_{XZ}\) for the corresponding
ordinary derivatives of \(F\) at \(X=Z=0\). If the left side of
(5) is \(\mathcal C[F]\), its first and mixed jets are
\[
\begin{split}
 \mathcal C[F]|_0&=\lambda[t^d]\mathscr M_aF_0,\\
 \partial_X\mathcal C[F]|_0
   &=\lambda[t^d]\mathscr M_a
           (F_X-\tau^{-1}D_{\tau^{-1},y}F_0),\\
 \partial_Z\mathcal C[F]|_0
   &=\lambda[t^d]\mathscr M_a
           (F_Z-\tau D_{\tau,c}F_0),\\
 \partial_X\partial_Z\mathcal C[F]|_0
   &=\lambda[t^d]\mathscr M_a
       (F_{XZ}-\tau^{-1}D_{\tau^{-1},y}F_Z
                    -\tau D_{\tau,c}F_X
                    +D_{\tau^{-1},y}D_{\tau,c}F_0).
\end{split} \tag{8}
\]
Here the merged substitution in each term is in \(c,y\).
In particular, replacing \(F\) by its protected-zero value before
applying the operator would lose actual neighboring derivatives.

## 3. Failure of descent to the fused attachment value

Formula (5) does not factor through the restriction
\(F\mapsto F(at,t)\). The exact polynomial test
\[
 F(c,y)=(c-ay)y^d
 \tag{9}
\]
vanishes identically on that diagonal. Nevertheless
\[
 D_{\tau^{-1},y}F
       =-\tau c y^{d-1},\qquad
 [X]\,\mathcal C[F](X,0)
       =\lambda(-\tau^{-1})(-\tau a)=\lambda a\ne0.
 \tag{10}
\]
We used \([d]_{\tau^{-1}}=-\tau\) and
\([N]_{\tau^{-1}}=0\), so the physical endpoint annihilation is
part of the calculation. This proves a failure of descent for
arbitrary polynomial attachments. It does not claim that (9) is
the source of a particular original knot or that such a knot has
a vanishing scalar.

## 4. Application to the actual marked normal form

The source-preserving mark choice in [U] leaves at most two boxes
containing both protected faces. In its nonbridge case, each such
box has four distinct face labels. If a selected box is a literal
signed crossing, name its protected outer and middle variables
\(X,Z\) and put the product of every other full box in \(F\).
Then (5) eliminates its two ordinary face targets exactly.
This is a concrete continuation of the phased corner merge [U, (8)]
to its full boundary neighborhood.

The entire neighboring kernel, every repeated incidence elsewhere,
and every occurrence of the same protected variable belong to \(F\).
They are differentiated before the merge. Expanding those derivatives
uses the shifted Jackson product rule, so it generally produces
shifted neighboring factors. Subsequent operations must retain this
whole expression; one may not first fuse values and then apply the
same formula to a discarded two-variable attachment.
If the protected global variables occupy the opposite order, rename
\(X,Z\) accordingly. Arbitrary coupons keep their actual kernels;
the one-crossing rule is not assigned to them.

For the full homogeneous original numerator of [U], the ordinary
targets have total degree \(dR\), equal to the numerator degree.
After *all* those targets are extracted, the result is therefore
independent of the restored protected variables. Every positive
protected occupation in that fully extracted expression is zero.
Equation (5) computes the intermediate boundary neighborhood and
its needed co-source data before that final extraction; it is not
a new scalar observable or a proof of a nonzero selected coefficient.
No absolute envelope, contour deformation, or asymptotic lower bound
is supplied by this exact operator identity.

## Complete direct sources

All complete texts and used implications were read. This proof uses
only written algebra, with no numerical or program evaluation.

| Label | Source | SHA-256 |
|---|---|---|
| J | [Original crossing Jackson boundary jets](research_crossing_jackson_boundary_jets.md) | 231d70047a49834c3df1f3cd722a704ec841c704a5213e5cf1d45caabc236bb7 |
| C | [Original protected cap-turn interface](research_trace_one_mark_and_cap_turn_interface.md) | d1be51d8fcaad2dd4886769ed5e172ceeaff66891c5cb1e46f29917d5ee97e48 |
| U | [Unique main-edge marked normal form](research_unique_main_mark_protected_corner_normal_form.md) | e621b399c9c6d2c96ced00b2042baf41f382d090f72090d1f9783f2fd49a685f |
